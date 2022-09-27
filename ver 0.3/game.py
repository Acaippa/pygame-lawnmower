import pygame
from modules.states.main_menu import *

class Game:
	def __init__(self, display):
		self.display_surface = pygame.display.get_surface()

		pygame.font.init()

		self.display = display # Display.py instance.

		self.delta_time = 0

		self.states = {
			"MainMenu" : MainMenu(self)
		}

		self.state = "MainMenu"

	def update(self, dt):
		self.delta_time = dt

		self.states[self.state].update(self.delta_time)