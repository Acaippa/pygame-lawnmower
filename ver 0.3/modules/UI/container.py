import pygame
import random

class Container:
	def __init__(self, parent, **kwargs):
		self.parent = parent

		self.container = kwargs.get("container", None)

		if self.container == None:
			self.parent.item_list.append(self)
		else:
			self.container.item_list.append(self)

		self.delta_time = 0

		self.size = kwargs.get("size", (20, 20))

		self.pos = kwargs.get("pos", (0, 0))

		self.overflow_int = kwargs.get("overflow", 2)

		self.padding = kwargs.get("padding", 0)

		self.item_list = []

		self.align = kwargs.get("align", "right")
		self.direction = kwargs.get("direction", "top")

		self.rect = pygame.Rect(self.pos, self.size)

	def update(self, dt):
		self.delta_time = dt

		self.update_items()

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
				self.x_pos = self.pos[0] + ((self.size[0] - x) / 10) * len(self.item_list)
			else:
				self.x_pos = self.pos[0]

			print(self.size[0] - x)

			if self.align == "center":
				self.x_pos = self.size[0] / 2
				self.y_pos = self.size[1] / 2

			if item.__class__.__name__ != "Container":
				item.pos = self.x_pos + (x + item.rect.width / 2 - item.rendered_font.get_width() / 2) + self.padding, self.y_pos + (y + item.rect.height / 2 - item.rendered_font.get_height() / 2) + self.padding # If x and y is larger than 0
			else:
				item.pos = self.x_pos + (x) + self.padding, self.y_pos + (y) + self.padding # If x and y is larger than 0

			x += (item.rect.width + self.padding) * x_dir
			y += (item.rect.height + self.padding) * y_dir

			item.update(self.delta_time)





