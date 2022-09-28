import pygame
from modules.game.grass import*

class Ground:
	def __init__(self, level):
		self.level = level

		self.display_surface = self.level.surface

		self.delta_time = 0

		w, h = self.display_surface.get_size()

		self.margin = 120

		self.background_color = "#094a16"

		self.surface = pygame.Surface((w-self.margin*2, h-self.margin*2))

		self.surface.fill(self.background_color)

		self.pos = (self.margin, self.margin)

	def update(self, dt):
		self.delta_time = dt

		self.draw()

	def draw(self):
		self.display_surface.blit(self.surface, self.pos)