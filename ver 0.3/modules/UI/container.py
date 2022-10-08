import pygame

class Container:
	def __init__(self, parent, **kwargs):
		self.parent = parent

		self.parent.item_list.append(self)

		self.delta_time = 0

		self.size = kwargs.get("size", (20, 20))

		self.pos = kwargs.get("pos", (0, 0))

		self.overflow_int = kwargs.get("overflow", 2)

		self.padding = kwargs.get("padding", 0)

		self.item_list = []

		self.direction = kwargs.get("direction", "left")

	def update(self, dt):
		self.delta_time = dt

		self.update_items()

		self.draw()

	def draw(self):
		pass

	def update_items(self):
		x, y = 0, 0

		for item in self.item_list:
			if self.direction == "right":
				x += 1

			elif self.direction == "left":
				x -= 1

			if self.direction == "top":
				y += 1

			elif self.direction == "bottom":
				y -= 1

			if x > 0 or x == 0:
				x_pos = self.pos[0]
			else:
				x_pos = self.size[0]

			if y > 0 or y == 0:
				y_pos = self.pos[0]
			else:
				y_pos = self.size[0]

			item.pos = x_pos + (item.rect.width * x), y_pos + (item.rect.height * y) # If x and y is larger than 0

			item.update(self.delta_time)





