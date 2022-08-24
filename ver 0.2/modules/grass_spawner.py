import pygame
import random
from modules.grass import*

class GrassSpawner:
	def __init__(self, ground):
		self.display_surface = pygame.display.get_surface()

		self.grass_list = []

		self.delta_time = 0

		self.grass_time = 0.5

		self.grass_index = 0

		self.ground = ground

	def update(self, dt):
		self.delta_time = dt

		self.update_grass()

		self.spawn_grass()

		self.draw()

	def draw(self):
		pass

	def update_grass(self):
		for grass in self.grass_list:
			grass.update(self.delta_time)


	def spawn_grass(self):
		w, h = self.ground.get_size()
		if self.grass_index >= self.grass_time:
			self.grass_list.append(grass())