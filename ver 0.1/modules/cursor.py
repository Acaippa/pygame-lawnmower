import pygame

class Cursor:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()
		self.width = 10
		self.surface_width = self.width * 2
		self.half_width = self.width // 2
		self.surface = pygame.Surface((self.surface_width, self.surface_width), pygame.SRCALPHA)

	def update(self):
		x, y = pygame.mouse.get_pos()
		pygame.draw.circle(self.surface, (255, 0, 0, 100), (self.surface_width // 2, self.surface_width // 2), self.width)
		self.display_surface.blit(self.surface, (x - self.width, y - self.width))
