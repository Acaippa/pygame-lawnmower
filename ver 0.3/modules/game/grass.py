import pygame
import random
from modules.game.grid import*

class Grass:
	def __init__(self, parent, **kwargs):
		self.parent = parent

		self.display_surface = parent.display_surface # Ground.py surface

		self.delta_time = 0

		self.pos = kwargs.get("pos", (0, 0))

		self.height = 10

		self.bend = random.uniform(-2, 2)

		self.color = kwargs.get("color", "#00af00")

		self.surface = pygame.Surface((6, self.height), pygame.SRCALPHA) #TODO: make the height of the surface dynamically change with the height of the grass

		self.mask = pygame.mask.from_surface(self.surface)

		self.calc_blit_pos()

	def update(self, dt):
		self.delta_time = dt

		self.update_surface()

		self.calc_blit_pos()

		self.draw()

	def draw(self):
		self.mask = pygame.mask.from_surface(self.surface)
		self.display_surface.blit(self.surface, self.blit_pos)

	def calc_blit_pos(self): # Draw the surface in the bottom center of the display_surface.
		self.blit_pos = (self.pos[0] + self.surface.get_width() / 2, self.pos[1] - self.surface.get_height())

	def update_surface(self): # Draw the line at the bottom center of the surface.
		x, y = self.surface.get_width() / 2, self.surface.get_height()
		self.rect = pygame.draw.line(self.surface, self.color, (x, y), (x + self.bend, y - self.height), width = 3)

	def remove_self(self):
		self.parent.grass_list.remove(self)