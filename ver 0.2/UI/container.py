import pygame

class Container:
	def __init__(self, **kwargs):
		self.display_surface = kwargs.get("surface", pygame.display.get_surface())

		self.container = kwargs.get("container", None)

		if self.container != None:
			self.container.add_item(self)
			self.display_surface = self.container.surface # Override the drawing surface for the container if its inside another container.

		self.item_list = []

		self.size = kwargs.get("size", (20, 20))

		self.pos = kwargs.get("pos", (0, 0))

		self.update_surface()

		self.delta_time = 0

	def update(self, dt):
		self.delta_time = dt

		self.update_surface()

		self.draw()

	def draw(self):
		self.display_surface.blit(self.surface, self.pos)

	def update_surface(self):
		self.surface = pygame.Surface(self.size, pygame.SRCALPHA)

		if self.display_surface != pygame.display.get_surface(): # If the surface of the container is set, make the container as big as the surface that is set.
			self.size = self.display_surface.get_size()

	def add_item(self, item):
		self.item_list.append(item)