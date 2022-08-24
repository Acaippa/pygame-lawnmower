import pygame
from settings import*

class Grass(pygame.sprite.Sprite):
	def __init__(self, pos, spawner):
		super().__init__(self)
		self.display_surface = pygame.display.get_surface()
		self.image = pygame.Surface((GRASS_SIZE, GRASS_SIZE))

		self.delta_time = 0

		self.pos = pos

		self.spawner = spawner

	def update(self, dt):
		self.delta_time = dt

		self.draw()

	def draw(self):
		self.display_surface.blit(self.image, self.pos)
