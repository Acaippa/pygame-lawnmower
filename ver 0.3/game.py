import pygame
from modules.states.main_menu import *
from modules.states.game_mode_menu import *
from modules.states.levels.test_level import *

class Game:
	def __init__(self, display):
		self.display_surface = pygame.display.get_surface()

		pygame.font.init()

		self.display = display # Display.py instance.

		self.delta_time = 0

		self.current_state = MainMenu(self)

		self.states = {
			"MainMenu" : MainMenu,
			"GameModeMenu" : GameModeMenu,
			
			"TestLevel" : TestLevel
		}

		self.state = "MainMenu"

	def update(self, dt):
		self.delta_time = dt

		self.current_state.update(self.delta_time)

	def change_state(self, state): # Change the state and init the state
		self.state = state
		self.current_state = self.states[self.state](self)
