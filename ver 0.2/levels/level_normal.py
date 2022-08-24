import pygame
from modules.ground import*

class LvlNormal:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()

		self.delta_time = 0

		self.ground = Ground()

	def update(self, dt):
		self.delta_time = dt
		
		self.ground.update(self.delta_time)
		
		self.draw()

	def draw(self):
		pass