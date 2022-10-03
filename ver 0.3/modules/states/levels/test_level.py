import pygame
from modules.game.ground import*
from modules.UI.player_info import*

class TestLevel:
	def __init__(self, parent):
		self.display_surface = pygame.display.get_surface()

		self.parent = parent

		self.surface = pygame.Surface(self.parent.display_surface.get_size())

		self.delta_time = 0

		self.pos = (0, 0)

		self.ground = Ground(self)

		self.player_info = PlayerInfo(self, pos=("center", 10), size=(500, 100))

	def update(self, dt):
		self.delta_time = dt

		self.player_info.update(self.delta_time)

		self.ground.update(self.delta_time)

		self.draw()

	def draw(self):
		self.display_surface.blit(self.surface, self.pos)