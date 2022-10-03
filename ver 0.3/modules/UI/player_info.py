import pygame
from modules.handlers.position_handler import *
from modules.UI.container import *
from modules.UI.text import *

class PlayerInfo:
	def __init__(self, level, **kwargs):
		self.level = level

		self.display_surface = self.level.surface

		self.font = kwargs.get("font", None)

		self.font_size = kwargs.get("font_size", 20)

		self.font = pygame.font.Font(self.font, self.font_size)

		self.pos = kwargs.get("pos", (0, 0))

		self.size = kwargs.get("size", (20, 20))

		self.surface = pygame.Surface(self.size)

		self.background_color = kwargs.get("background", "#2b2b2b")

		self.surface.fill(self.background_color)

		self.position_handler = PH(self)

		self.position_handler.parse_pos()

		self.rect = pygame.Rect(self.pos, self.size)

		self.font_color = kwargs.get("font_color", "#ffffff")

		self.item_list = []

		self.money_text = Text(self, text="Money: 0", pos=("center", 10), size=self.font_size, color=self.font_color)

		self.grass_text = Text(self, text="Grass: 0 / 1000", pos=("center", 50), size=self.font_size, color=self.font_color)

		self.delta_time = 0

	def update(self, dt):
		self.delta_time = dt

		self.update_items()

		self.draw()

	def draw(self):
		self.display_surface.blit(self.surface, self.pos)

	def update_items(self):
		for item in self.item_list:
			item.update(self.delta_time)

