import pygame
from modules.UI.text import *
from modules.UI.button import *
from modules.UI.container import *

class GameModeMenu:
	def __init__(self, parent, **kwargs):
		self.parent = parent

		self.display_surface = pygame.display.get_surface()

		self.delta_time = 0

		self.background_image = pygame.image.load("images/main_menu/background.png")

		w, h = self.display_surface.get_size()

		self.background_image = pygame.transform.scale(self.background_image, (w, h))

		self.surface = pygame.Surface((w, h))

		self.item_list = []

		self.main_container = Container(self, pos=(150, 160), size=(w-300, h-120), align="left", direction="right", padding=10)

		Button(self, container=self.main_container, text="Test_level", command=lambda: self.parent.change_state("TestLevel")) # Test level button.
		
		self.title = Text(self, text="Choose a Level!", pos=("center", 40), size=40)

	def update(self, dt):
		self.delta_time = dt
		self.draw_background()

		self.update_items()

		self.draw()

	def draw(self):
		self.display_surface.blit(self.surface, (0, 0))

	def draw_background(self):
		self.surface.fill("#ffffff")
		self.surface.blit(self.background_image, (0, 0))

	def update_items(self):
		for item in self.item_list:
			item.update(self.delta_time)