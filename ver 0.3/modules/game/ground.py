import pygame
from modules.game.grass import*
from modules.game.grid import*
from modules.states.levels.test_level_settings import*
import random

class Ground:
	def __init__(self, level):
		self.level = level

		self.display_surface = self.level.surface

		self.delta_time = 0

		w, h = self.display_surface.get_size()

		self.margin_x, self.margin_y = 40, 110 # Optimized margins making the size of the ground round.

		self.background_color = "#094a16"

		self.surface = pygame.Surface((w-self.margin_x*2, h-self.margin_y*2))

		self.surface.fill(self.background_color)

		self.pos = (self.margin_x, self.margin_y * 1.5) # Make Some extra space over the ground surface

		self.grid_list = []

		self.grid_index = 0

		self.total_grass = 0

		self.make_grids()

		self.pregrow()

	def update(self, dt):
		self.delta_time = dt
		self.surface.fill(self.background_color)

		if self.total_grass < GRASS_AMOUNT:
			self.spawn_grass()

		self.update_grids()

		self.draw()

	def draw(self):
		self.display_surface.blit(self.surface, self.pos)

	def make_grids(self):
		grid_amount_x, grid_amount_y = int(GRID.split("x")[0]), int(GRID.split("x")[1]) # Get the amount of grids in each dicrection.

		w, h = self.surface.get_size()

		grid_size_x, grid_size_y = w / grid_amount_x, h / grid_amount_y # Get the size of the grids by dividing the grid_amount by the width of the ground surface.

		for y in range(grid_amount_y):
			for x in range(grid_amount_x):
				self.grid_list.append(Grid(self, pos=(grid_size_x * x, grid_size_y * y), size=(grid_size_x, grid_size_y)))

	def update_grids(self):
		if self.grid_index < len(self.grid_list):
			self.grid_list[int(self.grid_index)].update(self.delta_time)
			self.grid_index += 100 * self.delta_time # Update 100 grids per second.
		else:
			self.grid_index = 0

		self.total_grass = 0

		mower = self.level.current_mower
		mower.grass_list.clear()

		for grid in self.grid_list: # Add the all the grass of the grids colliding with the mower to the mowers grass_list
			if grid.rect.colliderect(mower.cutting_rect):
				mower.grass_list.append(grid.grass_list)

			grid.draw()
			self.total_grass += len(grid.grass_list) # Increment the amount of grass by the amount of gass in the grid instance.

	def spawn_grass(self): # Get a random position inside the ground surface.
		w, h = self.surface.get_size()

		x, y = random.randint(0, w), random.randint(10, h)

		for grid in self.grid_list:
			if grid.rect.collidepoint((x, y)):
				grid.grass_list.append(Grass(grid, pos=(x, y)))

	def update_all_grids(self):
		for grid in self.grid_list:
			grid.update(self.delta_time)

	def pregrow(self): 
		for i in range(GRASS_AMOUNT):
			self.spawn_grass()

		self.update_all_grids()