import pygame
from modules.game.grass import*
from modules.game.grid import*

class Ground:
	def __init__(self, level):
		self.level = level

		self.display_surface = self.level.surface

		self.delta_time = 0

		w, h = self.display_surface.get_size()

		self.margin_x, self.margin_y = 40, 110 # Optimized margins making the size of the ground round.

		self.background_color = "#094a16"

		self.surface = pygame.Surface((w-self.margin_x*2, h-self.margin_y*2))

		self.surface.fill(self.background_color)

		self.pos = (self.margin_x, self.margin_y * 1.5)

		self.grid = Grid(self)

	def update(self, dt):
		self.delta_time = dt

		self.grid.update(dt)

		self.draw()

	def draw(self):
		self.display_surface.blit(self.surface, self.pos)