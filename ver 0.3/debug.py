import pygame

class Debug:
	def __init__(self, **kwargs):
		self.display_surface = pygame.display.get_surface()

		self.font = pygame.font.Font(None, 20)

		self.text = kwargs.get("text", "bruh")

		self.rendered_font = self.font.render(str(self.text), True, "#ffffff")

		self.display_surface.blit(self.rendered_font, (0, 0))