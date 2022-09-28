import pygame
from modules.game.ground import*

class TestLevel:
	def __init__(self, parent):
		self.display_surface = pygame.display.get_surface()

		self.parent = parent

		self.surface = pygame.Surface(self.parent.display_surface.get_size())

		self.delta_time = 0

		self.pos = (0, 0)

		self.ground = Ground(self)

	def update(self, dt):
		self.delta_time = dt

		self.ground.update(self.delta_time)

		self.draw()

	def draw(self):
		self.display_surface.blit(self.surface, self.pos)