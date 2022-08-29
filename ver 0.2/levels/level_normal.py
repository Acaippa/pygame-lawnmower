import pygame
from modules.ground import*
from modules.mower import*

class LvlNormal:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()

		self.delta_time = 0

		self.ground = Ground()

		self.test_mower = Mower01()

	def update(self, dt):
		self.delta_time = dt

		self.ground.update(self.delta_time, self.test_mower)

		self.test_mower.update(self.delta_time)
		
		self.draw()

	def draw(self):
		pass