import pygame
from modules.settings.json_manager import*

class Bag:
	def __init__(self, parent, **kwargs):
		self.parent = parent

		self.display_surface = self.parent.display_surface

		self.mower = kwargs.get("mower", None)

		self.dict = kwargs.get("dict", None)

		self.image_path = self.dict["image"]

		self.size = self.dict["size"]

		self.price = self.dict["price"]

		self.body_width, self.body_length = self.dict["body_width"], self.dict["body_length"]

		self.image = pygame.image.load(self.image_path).convert_alpha()

		self.image = pygame.transform.scale(self.image, self.size)

		self.rect = self.image.get_rect()

		self.pos = kwargs.get("pos", (0, 0))

		self.angle = self.mower.angle

		self.delta_time = 0

	def update(self, dt):
		self.delta_time = dt

		self.rotate()

		self.draw()

	def draw(self):
		self.display_surface.blit(self.rotated_image, self.rect)

	def rotate(self):
		self.angle = self.mower.angle

		self.rotated_image = pygame.transform.rotate(self.image, self.angle)

		self.rect = self.rotated_image.get_rect(center=self.pos)