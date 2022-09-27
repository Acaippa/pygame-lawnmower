import pygame
from modules.grass_spawner import*

class Ground:
	def __init__(self): # Ground at which grass spawns on.
		self.display_surface = pygame.display.get_surface()
		w, h = self.display_surface.get_size()
		self.margin = 20

		self.pos = (self.margin, self.margin * 3)

		self.size = (w-self.margin*2, h-self.margin*4)

		self.image = pygame.Surface(self.size)
		self.image.fill("#261808")

		self.rect = self.image.get_rect()

		self.mower = None

		self.delta_time = 0

		self.grass_spawner = GrassSpawner(self)

	def update(self, dt, mower):
		self.delta_time = dt
		self.mower = mower

		self.draw()

		self.grass_spawner.update(self.delta_time, self.mower)

	def draw(self):
		self.display_surface.blit(self.image, self.pos)

	def get_size(self):
		return self.size

	def get_pos(self):
		return self.pos

	def get_grass(self):
		return self.grass_spawner.get_grass()