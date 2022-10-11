import pygame

class Image:
	def __init__(self, parent, **kwargs):
		self.display_surface = parent.surface

		self.parent = parent

		self.container = kwargs.get("container", None)

		if self.container != None:
			self.container.item_list.append(self)

		self.image_path = kwargs.get("image", None)

		self.image = pygame.image.load(self.image_path).convert_alpha()

		self.pos = kwargs.get("pos", (0, 0))

		self.size = kwargs.get("size", (20, 20))

		self.image = pygame.transform.scale(self.image, self.size)

		self.rect = self.image.get_rect()

		self.delta_time = 0

		self.halt = False

	def update(self, dt):
		self.delta_time = dt

		self.draw()

	def draw(self):
		self.display_surface.blit(self.image, self.pos)