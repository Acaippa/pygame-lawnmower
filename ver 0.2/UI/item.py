import pygame

class item:
	def __init__(self, container):
		self.display_surface = pygame.display.get_surface()

		self.delta_time = 0

		self.container.add_item(self)

	def update(self, dt):
		self.delta_time = dt

		self.draw()

	def draw(self):
		pass