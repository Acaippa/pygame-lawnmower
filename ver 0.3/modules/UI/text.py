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

		self.parent.item_list.append(self)

		self.delta_time = 0

	def update(self, dt):
		self.delta_time = dt

		self.update_text()

		self.update_pos()

		self.draw()

	def draw(self):
		self.display_surface.blit(self.rendered_font, self.pos)

	def update_text(self):
		self.font = pygame.font.Font(self.settings["font_path"] + self.settings["font_name"], self.font_size)
		self.rendered_font = self.font.render(self.text, True, "#000000")

	def update_pos(self):
		if self.pos[0] == "center":
			self.pos = self.display_surface.get_width() / 2 - self.rendered_font.get_width() / 2, self.pos[1]

		if self.pos[1] == "center":
			self.pos = self.pos[0], self.display_surface.get_height() / 2 - self.rendered_font.get_height() / 2

		if self.pos[0] == "r":
			self.pos = self.display_surface.get_width() - self.rendered_font.get_width() - self.padding, self.pos[1]

		if self.pos[0] == "l":
			self.pos = 0 + self.rendered_font.get_width() + self.padding, self.pos[1]

		if self.pos[1] == "t":
			self.pos = self.pos[0], 0 + self.rendered_font.get_height() + self.padding

		if self.pos[1] == "b":
			self.pos = self.pos[1], self.display_surface.get_height() - self.rendered_font.get_height() - self.padding