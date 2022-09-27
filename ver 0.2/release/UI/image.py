import pygame

class Image:
	def __init__(self, **kwargs):
		self.container = kwargs.get("container", None)

		self.container.add_item(self)

		self.display_surface = self.container.surface if self.container != None else pygame.display.get_surface()

		self.pos = kwargs.get("pos", (0, 0))

		self.size = kwargs.get("size", (0, 0))

		self.rect = pygame.Rect(self.size, self.pos)

		self.adapt_bool = kwargs.get("adapt", None)

		self.image_path = kwargs.get("image", None)

		self.delta_time = 0

		self.update_size()

	def update(self, dt):
		self.delta_time = dt

		self.update_size()

		self.draw()

	def draw(self):
		self.display_surface.blit(self.surface, self.pos)

	def update_size(self):
		if self.adapt_bool:
			self.size = self.container.size

		self.surface = pygame.image.load(self.image_path).convert_alpha()

		self.surface = pygame.transform.scale(self.surface, self.size)