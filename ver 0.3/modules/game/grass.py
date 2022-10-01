import pygame
import random
from modules.game.grid import*

class Grass:
	def __init__(self, parent, **kwargs):
		self.parent = parent

		self.display_surface = self.parent.display_surface # Test_level surface

		self.delta_time = 0

		self.pos = kwargs.get("pos", (0, 0))

		self.height = 10

		self.bend = random.uniform(-2, 2)

		self.color = kwargs.get("color", "#00ff00")

	def update(self, dt):
		self.delta_time = dt

		self.draw()

	def draw(self):
		pygame.draw.line(self.display_surface, self.color, self.pos, (self.pos[0] + self.bend, self.pos[1] + self.height), width = 2)