import pygame
from modules.settings.json_manager import*

class Text:
	def __init__(self, parent, **kwargs):
		self.parent = parent

		self.display_surface = parent.surface

		self.settings = Load("settings.json")

		self.font_size = kwargs.get("size", 20)

		self.font = pygame.font.Font(self.settings["font_path"] + self.settings["font_name"], self.font_size)

		self.rect = pygame.Rect((20, 20), (20, 20))

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

	def update(self, dt):
		self.delta_time = dt

		if len(self.cmd_list) != 0:
			for cmd in self.cmd_list:
				cmd()

		self.update_text()

		self.update_pos()

		self.draw()

	def draw(self):
		self.rect.topleft = self.pos
		self.display_surface.blit(self.rendered_font, self.pos)

	def update_text(self):
		self.font = pygame.font.Font(self.settings["font_path"] + self.settings["font_name"], self.font_size)
		self.rendered_font = self.font.render(self.text, True, self.color)
		self.rect = self.rendered_font.get_rect()

	def update_pos(self):
		w, h = self.display_surface.get_size() if self.container == None else self.container.size

		if self.pos[0] == "center":
			self.pos = w / 2 - self.rendered_font.get_width() / 2, self.pos[1]

		if self.pos[1] == "center":
			self.pos = self.pos[0], h / 2 - self.rendered_font.get_height() / 2

		if self.pos[0] == "r":
			self.pos = w - self.rendered_font.get_width() - self.padding, self.pos[1]

		if self.pos[0] == "l":
			self.pos = 0 + self.rendered_font.get_width() + self.padding, self.pos[1]

		if self.pos[1] == "t":
			self.pos = self.pos[0], 0 + self.rendered_font.get_height() + self.padding

		if self.pos[1] == "b":
			self.pos = self.pos[1], h - self.rendered_font.get_height() - self.padding
