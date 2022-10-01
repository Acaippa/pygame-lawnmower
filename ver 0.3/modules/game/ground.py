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

		self.pos = (self.margin_x, self.margin_y * 1.5)

		self.grid_list = []

		self.make_grids()

	def update(self, dt):
		self.delta_time = dt

		self.spawn_grass()

		self.update_grids()

		self.draw()

	def draw(self):
		self.display_surface.blit(self.surface, self.pos)

	def make_grids(self):
		grid_amount_x, grid_amount_y = int(GRID.split("x")[0]), int(GRID.split("x")[1])

		w, h = self.display_surface.get_size()

		grid_size_x, grid_size_y = w / grid_amount_x, h / grid_amount_y

		for y in range(grid_amount_y):
			for x in range(grid_amount_x):
				self.grid_list.append(Grid(self, pos=(grid_size_x * x, grid_size_y * y), size=(grid_size_x, grid_size_y)))

	def update_grids(self):
		for grid in self.grid_list:
			grid.update(self.delta_time)

	def spawn_grass(self):
		w, h = self.display_surface.get_size()

		x, y = random.randint(0, self.pos[0] + w), random.randint(0, self.pos[1] + h)

		for grid in self.grid_list:
			if grid.rect.collidepoint((x, y)):
				grid.grass_list.append(Grass(grid, pos=(x, y)))