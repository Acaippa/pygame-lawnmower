import pygame
from modules.grass_spawner import*

class Ground:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()
		w, h = self.display_surface.get_size()
		self.margin = 20

		self.pos = (self.margin, self.margin)

		self.size = (w-self.margin*2, h-self.margin*2)

		self.image = pygame.Surface(self.size)
		self.image.fill("#452203")

		self.delta_time = 0

		self.grass_spawner = GrassSpawner(self)

	def update(self, dt):
		self.delta_time = dt

		self.grass_spawner.update(self.delta_time)

		self.draw()

	def draw(self):
		self.display_surface.blit(self.image, self.pos)


	def get_size(self):
		return