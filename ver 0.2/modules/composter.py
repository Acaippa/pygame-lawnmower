import pygame
from settings import*

class Composter:
	def __init__(self, mower):
		self.display_surface = pygame.display.get_surface()
		self.image = pygame.image.load("images/composter.png")
		w, h, = self.image.get_size()
		self.image = pygame.transform.scale(self.image, (w * MOWER_SIZE, h * MOWER_SIZE))
		
		self.delta_time = 0

		self.pos = (0, self.display_surface.get_height())

		self.velocity = 1

		self.mower = mower

	def update(self, dt):
		self.delta_time = dt

		if self.mower.bag.attached_to_mower:
			self.show_self()

		self.draw()

	def draw(self):
		self.display_surface.blit(self.image, self.pos)

	def show_self(self):
		if self.pos[1] > 0:
			self.pos = self.pos[0], self.pos[1] - self.velocity