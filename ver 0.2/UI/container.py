import pygame

class Container:
	def __init__(self, **kwargs):
		self.display_surface = kwargs.get("surface", pygame.display.get_surface())

		self.container = kwargs.get("container", None)

		if self.container != None:
			self.container.add_item(self)
			self.display_surface = self.container.surface # Override the drawing surface for the container if its inside another container.
			print(self.container.surface)

		self.item_list = []

		self.size = kwargs.get("size", (20, 20))

		self.pos = kwargs.get("pos", (0, 0))

		self.overflow_int = kwargs.get("overflow", 2)

		self.padding = kwargs.get("padding", 0)

		self.background_color = kwargs.get("background", None)

		self.update_surface()

		self.delta_time = 0

	def update(self, dt):
		self.delta_time = dt

		self.update_surface()

		if len(self.item_list) > 0:
			self.update_items()

		self.draw()

	def draw(self):
		self.display_surface.blit(self.surface, self.pos)

	def update_surface(self):
		if self.background_color != None:
			self.surface = pygame.Surface(self.size)
			self.surface.fill(self.background_color)
		else:
			self.surface = pygame.Surface(self.size, pygame.SRCALPHA)

		if self.display_surface != pygame.display.get_surface(): # If the surface of the container is set, make the container as big as the surface that is set.
			self.size = self.display_surface.get_size()

	def update_items(self):
		y = 0
		x = -1

		for item in self.item_list:
			if x != self.overflow_int -1:
				x += 1
			else:
				x = 0
				y += 1

			# Change the width of the item to be the width of the container divided by the amount of items per row minus the padding of the items.
			item.size = (self.size[0] - self.padding * 3) // self.overflow_int, (self.size[0] - self.padding * 3) // self.overflow_int
			item.pos = (item.size[0] + self.padding) * x + self.padding, (item.size[1] + self.padding) * y + self.padding

			self.surface.blit(item.surface, item.pos)
			item.update(self.delta_time)

	def add_item(self, item):
		self.item_list.append(item)