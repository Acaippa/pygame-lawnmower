import pygame
from settings import*
from game import*
from debug import*

class Display:
	def __init__(self):
		self.display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
		self.running = True

		self.game = Game()

		self.delta_time = 0

		self.clock = pygame.time.Clock()

	def close(self):
		self.running = False

	def main_loop(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.close()

			self.display_surface.fill("black")

			self.game.update(self.delta_time)

			self.delta_time = self.clock.tick(60)
			showfps(self.clock.get_fps()) # Debug
			pygame.display.flip()