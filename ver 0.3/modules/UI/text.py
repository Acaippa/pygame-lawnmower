import pygame
from modules.settings.json_manager import*

class Text:
	def __init__(self, parent, **kwargs):
		self.parent = parent

		self.display_surface = parent.surface

		self.settings = Load("settings.json")

		self.font_size = kwargs.get("size", 20)

		self.font = pygame.font.Font(self.settings["font_path"] + self.settings["font_name"], self.font_size)

		self.text = kwargs.get("text", " ")

		self.pos = kwargs.get("pos", (0, 0))

		self.padding = kwargs.get("padding", 0)

		self.color = kwargs.get("color", "#ffffff")

		self.cmd_list = [] # Used by other modules

		self.container = kwargs.get("container", None)

		if self.container != None:
			self.container.item_list.append(self)
		else:
			self.parent.item_list.append(self)

		self.delta_time = 0

		self.update_text()

		self.halt = False

	def update(self, dt):
		self.delta_time = dt

		if not self.halt:
			self.update_text()

			self.update_pos()

			self.update_rect()

			if len(self.cmd_list) != 0:
				for cmd in self.cmd_list:
					cmd()

			self.draw()

	def draw(self):
		self.display_surface.blit(self.image, self.pos)

	def update_text(self):
		self.image = self.font.render(self.text, True, self.color)
		self.rect = self.image.get_rect()
		
	def update_pos(self):
		w, h = self.display_surface.get_size() if self.container == None else self.container.size

		if self.pos[0] == "center":
			self.pos = w / 2 - self.image.get_width() / 2, self.pos[1]

		if self.pos[1] == "center":
			self.pos = self.pos[0], h / 2 - self.image.get_height() / 2

		if self.pos[0] == "r":
			self.pos = w - self.image.get_width() - self.padding, self.pos[1]

		if self.pos[0] == "l":
			self.pos = 0 + self.image.get_width() + self.padding, self.pos[1]

		if self.pos[1] == "t":
			self.pos = self.pos[0], 0 + self.image.get_height() + self.padding

		if self.pos[1] == "b":
			self.pos = self.pos[1], h - self.image.get_height() - self.padding

	def update_rect(self):
		self.rect.topleft = self.pos
