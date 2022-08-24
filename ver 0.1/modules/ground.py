import pygame


class Ground:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()
		self.background_color = ("#3D1D00")
		self.surface = pygame.surface.Surface((self.display_surface.get_size()[0] - 40, self.display_surface.get_size()[1] - 40))
		self.surface.fill(self.background_color)

	def draw(self):
		self.display_surface.blit(self.surface, (20, 20))