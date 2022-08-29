import pygame
from random import*
from modules.grass import*
from math import*
from threading import*

class GrassSpawner:
	def __init__(self, ground):
		self.display_surface = pygame.display.get_surface()

		self.grass_list = []

		self.delta_time = 0

		self.grass_time = 0.01

		self.grass_index = 0

		self.ground = ground

		self.grass_rate = 1 # The rate at which the grass_index increases.

		self.grass_per_frame = 50

		self.mower = None

	def update(self, dt, mower):
		self.delta_time = dt
		self.mower = mower

		self.spawn_grass()

		self.update_grass()

		self.cut_grass()

		self.draw()

	def draw(self):
		pass

	def update_grass(self):
		for grass in self.grass_list:
			grass.update(self.delta_time)

	def spawn_grass(self): # Get random coordinates inside ground and spawn grass.
		if self.grass_index >= self.grass_time and len(self.grass_list) < MAX_GRASS_AMOUNT:
			for i in range(self.grass_per_frame):
				# Width and height of ground.
				w, h = self.ground.get_size()
				# The start of X and Y of the ground.
				x, y = self.ground.get_pos()
				grass_x, grass_y = randint(x, x+w), randint(y, y+h)
				self.grass_list.append(Grass((grass_x, grass_y), self))
			self.grass_index = 0
		else:
			self.grass_index += self.grass_rate * self.delta_time

	def cut_grass(self): # Check if the certain close grass is colliding with the mower.
		for grass in self.grass_list:
			if sqrt((self.mower.pos[0] - grass.pos[0])**2 + (self.mower.pos[1] - grass.pos[1])**2) < 30:
				offset_x = grass.rect[0] - self.mower.rotated_cutting_surface_rect[0]
				offset_y = grass.rect[1] - self.mower.rotated_cutting_surface_rect[1]
				if self.mower.rotated_cutting_mask.overlap(grass.mask, (offset_x, offset_y)) != None:
					grass.on_collision()

	def get_grass(self):
		return self.grass_list
