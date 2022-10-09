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

		self.align = kwargs.get("align", "right")
		self.direction = kwargs.get("direction", "top")

	def update(self, dt):
		self.delta_time = dt

		self.update_items()

		self.draw()

	def draw(self):
		pass

	def update_items(self):
		x_dir, y_dir = 0, 0
		x, y = 0, 0
		step = 0

		for item in self.item_list:
			if self.direction == "right":
				x_dir = 1

			elif self.direction == "left":
				x_dir = -1

			if self.direction == "bottom":
				y_dir = 1

			elif self.direction == "top":
				y_dir = -1


			if self.align == "top":
				self.y_pos = self.pos[1]
			elif self.align == "bottom":
				self.y_pos = self.size[1]
			elif self.align == "centery":
				self.y_pos = self.size[1] / 2
			else:
				self.y_pos = self.pos[1]

			if self.align == "right":
				self.x_pos = self.size[0]
			elif self.align == "left":
				self.x_pos = self.pos[0]
			elif self.align == "centerx":
				self.x_pos = self.size[0] / 2
			else:
				self.x_pos = self.pos[0]

			if self.align == "center":
				self.x_pos = self.size[0] / 2
				self.y_pos = self.size[1] / 2

			item.pos = (self.x_pos) + x, (self.y_pos) + y # If x and y is larger than 0

			x += (item.rect.width + self.padding) * x_dir
			y += (item.rect.height + self.padding) * y_dir

			item.update(self.delta_time)





