import pygame
from modules.UI.text import *
from modules.UI.button import *

class MainMenu:
	def __init__(self, parent):
		self.display_surface = pygame.display.get_surface()

		self.parent = parent

		self.delta_time = 0

		w, h, = self.display_surface.get_size()

		self.surface = pygame.Surface((w, h))

		self.background_image = pygame.image.load("images/main_menu/background.png").convert_alpha()

		self.background_image = pygame.transform.scale(self.background_image, (w, h))

		self.item_list = [] # Buttons, text etc.

		self.title = Text(self, text="Mowe lawn, Mowe!", pos=("center", 40), size=50)
		self.play_button = Button(self, text="Play", pos=("center", 190), size=30, command=lambda: self.parent.change_state("GameModeMenu"))

	def update(self, dt):
		self.delta_time = dt
		
		self.draw_background()

		self.update_items()

		self.draw()

	def draw(self):
		self.display_surface.blit(self.surface, (0,0))

	def update_items(self): # Update buttons, text etc.
		for i in self.item_list:
			i.update(self.delta_time)

	def draw_background(self):
		self.surface.fill("white")
		self.surface.blit(self.background_image, (0,0))