import pygame
from modules.settings.json_manager import*
from game import*

class Display:
	def __init__(self):
		self.settings = Load("settings.json")

		width, height = self.settings["win_width"], self.settings["win_height"]

		self.display_surface = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

		self.fps = self.settings["fps"]

		self.actual_fps = 0

		self.running = True

		self.delta_time = 0

		self.clock = pygame.time.Clock()

		self.game = Game(self)

	def main_loop(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

			self.display_surface.fill("black")

			self.game.update(self.delta_time)

			self.delta_time = self.clock.tick(self.fps) / 1000
			self.actual_fps = self.clock.get_fps()
			pygame.display.flip()