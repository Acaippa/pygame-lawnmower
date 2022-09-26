import pygame

class MainMenu:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()

		self.delta_time = 0

		w, h, = self.display_surface.get_size()

		self.surface = pygame.Surface((w, h))

		self.background_image = pygame.image.load("images/main_menu/background.png").convert_alpha()

		self.background_image = pygame.transform.scale(self.background_image, (w, h))

	def update(self, dt):
		self.delta_time = dt

		self.draw()

	def draw(self):
		self.surface.fill("white")
		self.surface.blit(self.background_image, (0,0))
		self.display_surface.blit(self.surface, (0,0))