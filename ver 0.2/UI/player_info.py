import pygame

class PlayerInfo:
	def __init__(self, mower):
		self.display_surface = pygame.display.get_surface()
		pygame.font.init()
		self.margin = 50

		self.mower = mower

		self.pos = self.margin, 0

		w, h = self.display_surface.get_size()
		self.surface = pygame.Surface((w - self.margin * 2, 50))

		self.background_color = "#212126"

		self.surface.fill(self.background_color)

		self.delta_time = 0

	def update(self, dt):
		self.delta_time = dt

		self.surface.fill(self.background_color)

		self.write(f"$ {self.mower.get_grass_cut()}", pos=("center", 0), size=30)

		self.draw()

	def draw(self):
		self.display_surface.blit(self.surface, self.pos)

	def write(self, text, **kwargs):
		pos = kwargs.get("pos", (0, 0))
		size = kwargs.get("size", 20)

		font = pygame.font.Font(None, size)

		self.rendered_font = font.render(str(text), True, "#ffffff")
		if pos[0] == "center":
			pos = self.surface.get_width() // 2 - self.rendered_font.get_width() // 2, pos[1]

		if pos[1] == "center":
			pos = pos[0], self.surface.get_height() // 2 - self.rendered_font.get_height() // 2
		self.surface.blit(self.rendered_font, pos)