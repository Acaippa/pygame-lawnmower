import pygame
from levels.level_normal import*

class Game:
	def __init__(self):
		self.delta_time = 0

		self.level_list = {
			"lvlnormal" : LvlNormal()
		}

		self.level_state = "lvlnormal"

	def update(self, dt):
		self.delta_time = dt

		self.level_list[self.level_state].update(self.delta_time) # Update right level state.

	def draw(self):
		pass