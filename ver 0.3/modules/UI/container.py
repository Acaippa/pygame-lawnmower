import pygame

class Container:
	def __init__(self, parent, **kwargs):
		self.display_surface = pygame.display.get_surface()

		self.parent = parent

		self.parent.item_list.append(self)

		self.delta_time = 0

		self.size = kwargs.get("size", (20, 20))

		self.pos = kwargs.get("pos", (0, 0))

		self.overflow_int = kwargs.get("overflow", 2)

		self.padding = kwargs.get("padding", 0)

		self.item_list = []

	def update(self, dt):
		self.delta_time = dt

		self.update_items()

		self.draw()

	def draw(self):
		pass

	def update_items(self):
		for index, item in enumerate(self.item_list):
			offset_x = self.pos[0]
			offset_y = self.pos[1] + (item.rect.height + self.padding + item.padding) * index

			item.pos = item.pos[0] + offset_x, item.pos[1] + offset_y

			item.update(self.delta_time)
			item.pos = item.pos[0] - offset_x, item.pos[1] - offset_y

