import pygame
from random import*
from modules.grass import*
from math import*
from threading import*
from settings import*

class GrassSpawner:
	def __init__(self, ground):
		self.display_surface = pygame.display.get_surface()

		self.delta_time = 0

		self.grass_time = 0.1

		self.grass_index = 0

		self.ground = ground

		self.grass_rate = 1 # The rate at which the grass_index increases.

		self.mower = None

		self.grid_list = []

		self.total_grass = 0

		self.grid_index = 0

		self.make_grid()

	def update(self, dt, mower):
		self.delta_time = dt
		self.mower = mower

		self.update_grids()

		self.spawn_grass()

		self.draw()

	def draw(self):
		pass

	def spawn_grass(self): # Get random coordinates inside ground and spawn grass.
		if self.grass_index >= self.grass_time and self.total_grass + GRASS_PER_FRAME <= MAX_GRASS_AMOUNT:
			for i in range(GRASS_PER_FRAME):
				ground_x, ground_y = self.ground.pos
				ground_width, ground_height = self.ground.rect.width, self.ground.rect.height

				random_ground_x, random_ground_y = randint(ground_x, ground_x + ground_width), randint(ground_y, ground_y + ground_height)

				for grid in self.grid_list:
					if grid.rect.collidepoint(random_ground_x, random_ground_y):
						grid.add_grass(Grass((random_ground_x, random_ground_y), self))

			self.grass_index = 0
		else:
			self.grass_index += self.grass_rate * self.delta_time

	def get_grass(self):
		return self.grass_list

	def make_grid(self):
		dimentions = GRID_DIMENTIONS.split("x")

		grid_width = self.ground.rect.width / int(dimentions[0])
		grid_height = self.ground.rect.height / int(dimentions[1])

		for y in range(int(dimentions[1])):
			for x in range(int(dimentions[0])):
				self.grid_list.append(Grid(self.ground, (x, y), (grid_width, grid_height)))

	def update_grids(self):
		if self.grid_index < len(self.grid_list):
			self.grid_list[self.grid_index].update(self.delta_time)
			self.grid_index += 1
		else:
			self.grid_index = 0

		# Get total amount of grass
		self.total_grass = 0

		for grid in self.grid_list:
			grid.draw()
			if grid.rect.colliderect(self.mower.rotated_cutting_surface_rect):
				grid.update(self.delta_time)
			self.total_grass += len(grid.grass_list)

class Grid:
	def __init__(self, ground, pos, dim):
		self.display_surface = pygame.display.get_surface()

		self.pos = pos

		self.dimentions = dim

		self.delta_time = 0

		self.ground = ground

		x, y = (self.ground.pos[0] + self.dimentions[0] * self.pos[0], self.ground.pos[1] + self.dimentions[1] * self.pos[1])
		w, h = self.dimentions[0], self.dimentions[1]
		self.rect = pygame.Rect(x, y, w, h)

		self.grass_list = []

	def update(self, dt):
		self.delta_time = dt

		self.mower = self.ground.mower

		for grass in self.grass_list:
			grass.update(self.delta_time)

		self.cut_grass()

	def draw(self):
		for grass in self.grass_list:
			grass.draw()

	def add_grass(self, grass):
		self.grass_list.append(grass)

	def cut_grass(self): # Check if the certain close grass is colliding with the mower.
		if self.mower != None:
			for grass in self.grass_list:
				if sqrt((self.mower.pos[0] - grass.pos[0])**2 + (self.mower.pos[1] - grass.pos[1])**2) < 30:
					offset_x = grass.rect[0] - self.mower.rotated_cutting_surface_rect[0]
					offset_y = grass.rect[1] - self.mower.rotated_cutting_surface_rect[1]
					if self.mower.rotated_cutting_mask.overlap(grass.mask, (offset_x, offset_y)) != None:
						grass.on_collision(self)
						self.mower.on_collision()