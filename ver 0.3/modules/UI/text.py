import pygame
from modules.settings.json_manager import*

class Text:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()

		self.settings = Load("settings.py")

		