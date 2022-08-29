import pygame

class showfps: # Render the FPS on the screen.
	def __init__(self, fps):
		self.display_surface = pygame.display.get_surface()
		pygame.font.init()
		self.font = pygame.font.SysFont(None, 20)
		self.rendered_font = self.font.render(str(int(fps)), True, "#ffffff")
		self.display_surface.blit(self.rendered_font, (0, 0))