import pygame
import random

class Container:
	def __init__(self, parent, **kwargs):
		self.parent = parent

		self.display_surface = self.parent.surface

		self.container = kwargs.get("container", None)

		if self.container == None:
			self.parent.item_list.append(self)
		else:
			self.container.item_list.append(self)

		self.delta_time = 0

		self.size = kwargs.get("size", (20, 20))

		self.pos = kwargs.get("pos", (0, 0))

		self.padding = kwargs.get("padding", 0)
		self.padding_between = kwargs.get("padding_between", 0)

		self.size = self.size[0] + self.padding * 2, self.size[1] + self.padding * 2

		self.item_list = []

		self.align = kwargs.get("align", "right")
		self.direction = kwargs.get("direction", "top")

		self.rect = pygame.Rect(self.pos, self.size)

		self.halt = False

		self.background_color = kwargs.get("background", None)

		self.surface = pygame.Surface(self.size, pygame.SRCALPHA)

		if self.background_color != None:
			self.surface.fill(self.background_color)

		self.click_check = True

		self.command = self.fallback_command


	def update(self, dt):
		self.delta_time = dt

		self.draw()

		if not self.halt:
			self.update_items()

		self.hover()

	def update_items(self):
		x_dir, y_dir = 0, 0
		x, y = 0, 0

		for item in self.item_list:
			if item.halt != True:
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
					self.x_pos = self.pos[0] / 2
				else:
					self.x_pos = self.pos[0]

				if self.align == "center":
					self.x_pos = self.size[0] / 2
					self.y_pos = self.size[1] / 2

				try:
					item.pos = self.x_pos + (x + item.rect.width / 2 - item.image.get_width() / 2) + self.padding, self.y_pos + (y + item.rect.height / 2 - item.image.get_height() / 2) + self.padding # If x and y is larger than 0
				except Exception as e:
					item.pos = self.x_pos + (x + self.padding * 2), self.y_pos + (y + self.padding * 2)

				if x > self.size[0]:
					y += (item.rect.height + self.padding_between)
					x = - (item.rect.width + self.padding_between)

				x += (item.rect.width + self.padding_between) * x_dir
				y += (item.rect.height + self.padding_between) * y_dir

				item.update(self.delta_time)

	def draw(self):
		self.display_surface.blit(self.surface, self.pos)

	def hover(self):
		mouse_pos = pygame.mouse.get_pos()[0] - self.parent.pos[0], pygame.mouse.get_pos()[1] - self.parent.pos[1]
		mouse_clicked = pygame.mouse.get_pressed()

		if self.rect.collidepoint(mouse_pos) and mouse_clicked[0]:
			self.click_check = True

		if self.rect.collidepoint(mouse_pos) and mouse_clicked[0] == False and self.click_check:
			self.command()
			self.click_check = False

	def fallback_command(self):
		print(__name__, " Has no function yet.")





