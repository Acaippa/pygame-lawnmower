import pygame

class TestLevel:
	def __init__(self, parent):
		self.parent = parent

		self.surface = pygame.Surface(self.parent.display_surface.get_size())

		self.delta_time = 0

	def update(self, dt):
		self.delta_time = dt

		self.draw()

	def draw(self):
		pass