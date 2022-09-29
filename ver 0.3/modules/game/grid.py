import pygame
from modules.states.levels.test_level_settings import*

class Grid:
	def __init__(self, parent, **kwargs):
		self.parent = parent # Ground.py

		self.pos = kwargs.get("pos", (0, 0))

		self.grass_list = []

		self.delta_time = 0

	def update(self, dt):
		self.delta_time = dt

		self.update_grass()

	def update_grass(self):
		for grass in self.grass_list:
			grass.update()

