import pygame
import math

class LawnMower(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.image = pygame.image.load("images/mower.png")
		self.mask = pygame.mask.from_surface(self.image)
		self.x, self.y = 0,0
		self.rect = pygame.rect.Rect(self.x, self.y, self.image.get_width() + 20, self.image.get_height() + 20)
		self.rect.center = (self.x, self.y)
		self.angle = 0

		self.cutter = pygame.Surface((60, 90), pygame.SRCALPHA)
		self.cutter.fill("#ffffff")
		self.cutter_rect = self.cutter.get_rect(center=(self.x, self.y))

	def update(self, dt):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			rads = math.radians(self.angle)
			self.x, self.y = self.x - 1*math.sin(rads), self.y - 1*math.cos(rads)

		if keys[pygame.K_d]:
			self.angle -= 100 * dt

		if keys[pygame.K_a]:
			self.angle += 100 * dt

		self.image_to_show = pygame.transform.rotate(self.image, self.angle)
		self.rect = self.image_to_show.get_rect(center=(self.x, self.y))

		self.cutter_to_show = pygame.transform.rotate(self.cutter, self.angle)
		self.cutter_rect = self.cutter_to_show.get_rect(center=(self.x, self.y))

		self.display_surface.blit(self.image_to_show, self.rect)

