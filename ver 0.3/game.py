import pygame
from modules.states.main_menu import *
from modules.states.game_mode_menu import *
from modules.states.levels.test_level import*

class Game:
	def __init__(self, display):
		self.display_surface = pygame.display.get_surface()

		pygame.font.init()

		self.display = display # Display.py instance.

		self.delta_time = 0

		self.states = {
			"MainMenu" : MainMenu(self),
			"GameModeMenu" : GameModeMenu(self),
			
			"TestLevel" : TestLevel(self)
		}

		self.state = "MainMenu"

	def update(self, dt):
		self.delta_time = dt

		self.states[self.state].update(self.delta_time)

	def change_state(self, state):
		self.state = state