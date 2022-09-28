import pygame
from modules.states.levels.test_level_settings import*

class Grid:
	def __init__(self, parent, **kwargs):
		self.parent = parent # Ground.py

		self.display_surface = self.parent.display_surface

		self.parent_width, self.parent_height = self.parent.surface.get_size()

		self.grid_division_x, self.grid_division_y = GRID.split("x")
		self.grid_division_x, self.grid_division_y = int(self.grid_division_x), int(self.grid_division_y) 


		self.delta_time = 0

	def update(self, dt):
		self.delta_time = dt

		self.draw()

	def draw(self):
		pass