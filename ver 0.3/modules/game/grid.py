import pygame
from modules.states.levels.test_level_settings import*

class Grid:
	def __init__(self, parent, **kwargs): # The grid holds all the grass inside its own area.
		self.parent = parent # Ground.py

		self.display_surface = parent.surface

		self.pos = kwargs.get("pos", (0, 0))

		self.size = kwargs.get("size", (0, 0))

		self.rect = pygame.Rect(self.pos, self.size)

		self.grass_list = []

		self.delta_time = 0

	def update(self, dt):
		self.delta_time = dt

		self.update_grass()

	def update_grass(self):
		for grass in self.grass_list:
			grass.update(self.delta_time)

	def draw(self):
		for grass in self.grass_list:
			grass.draw()

