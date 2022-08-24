import pygame
from modules.ground import*
from modules.grass import*
from modules.grass_spawner import*
from modules.lawn_mower import*

class Main:
	def __init__(self, width = 800, height = 600, fullscreen = False):
		self.screen = pygame.display.set_mode((width, height))
		self.ground = Ground()
		self.grass_spawner = GrassSpawner()
		self.lawn_mower = LawnMower()

		self.running = True
		self.clock = pygame.time.Clock()

		self.delta_time = 0

		self.main_loop()

	def main_loop(self): # Main game loop.
		while self.running:
			self.screen.fill("#000000")
			self.check_if_closed()

			self.ground.draw()

			self.grass_spawner.update(self.lawn_mower)
			self.lawn_mower.update(self.delta_time)

			pygame.display.flip()
			self.delta_time = self.clock.tick(60) / 1000


	def check_if_closed(self): # Check if the user has clicked the exit button.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False


main = Main()