import pygame
from settings import*

class Composter:
	def __init__(self, mower):
		self.display_surface = pygame.display.get_surface()
		self.image = pygame.image.load("images/composter.png")
		w, h, = self.image.get_size()
		self.image = pygame.transform.scale(self.image, (w * MOWER_SIZE, h * MOWER_SIZE))
		
		self.delta_time = 0

		w, h = self.display_surface.get_size()
		self.pos = (w / 2, h)

		self.velocity = 100

		self.mower = mower

		self.rect = self.image.get_rect(center = self.pos)

	def update(self, dt):
		self.delta_time = dt

		if not self.mower.bag.attached_to_mower:
			self.show_self()
		else:
			self.hide_self()

		self.draw()

	def draw(self):
		self.rect = self.image.get_rect(center = self.pos)
		self.display_surface.blit(self.image, (self.pos[0] - self.image.get_width() / 2, self.pos[1]))

	def show_self(self):
		if self.pos[1] > self.display_surface.get_height() - self.image.get_height():
			self.pos = self.pos[0], self.pos[1] - self.velocity * self.delta_time

	def hide_self(self):
		if self.pos[1] < self.display_surface.get_height():
			self.pos = self.pos[0], self.pos[1] + self.velocity * self.delta_time