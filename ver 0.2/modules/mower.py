import pygame
import math
from settings import*

class Mower(pygame.sprite.Sprite):
	def __init__(self, image, pos):
		pygame.sprite.Sprite.__init__(self)
		self.display_surface = pygame.display.get_surface()

		self.image = pygame.image.load(image).convert_alpha()
		w, h = self.image.get_size()
		self.image = pygame.transform.scale(self.image, (w * MOWER_SIZE, h * MOWER_SIZE))

		self.pos = pos

		self.delta_time = 0

		self.rect = self.image.get_rect(center=self.pos)

		self.angle = 0

		self.speed = 40

		self.turn_rate = 100

		self.cutting_surface = pygame.Surface((30, 40), pygame.SRCALPHA)
		self.cutting_surface.fill("#ffffff")

		self.rotated_cutting_surface = pygame.transform.rotate(self.cutting_surface, self.angle)
		self.rotated_cutting_surface_rect = self.rotated_cutting_surface.get_rect(center = self.pos)

		self.cutting_mask = pygame.mask.from_surface(self.rotated_cutting_surface)

	def update(self, dt):
		self.delta_time = dt
		
		self.process_input()

		self.rotate()

		self.draw()

	def draw(self):
		self.display_surface.blit(self.rotated_image, self.rect)

	def process_input(self):
		keys = pygame.key.get_pressed()

		radians = math.radians(self.angle)

		if keys[pygame.K_UP]:
			self.pos = self.pos[0] - (math.sin(radians) * self.speed) * self.delta_time, self.pos[1] - (math.cos(radians) * self.speed) * self.delta_time

		if keys[pygame.K_DOWN]:
			self.pos = self.pos[0] + (math.sin(radians) * self.speed) * self.delta_time, self.pos[1] + (math.cos(radians) * self.speed) * self.delta_time

		if keys[pygame.K_RIGHT]:
			self.angle -= self.turn_rate * self.delta_time

		if keys[pygame.K_LEFT]:
			self.angle += self.turn_rate * self.delta_time

	def rotate(self):
		self.rotated_image = pygame.transform.rotate(self.image, self.angle)
		self.rect = self.rotated_image.get_rect(center=self.pos)

		self.rotated_cutting_surface = pygame.transform.rotate(self.cutting_surface, self.angle)
		self.rotated_cutting_surface_rect = self.rotated_cutting_surface.get_rect(center = self.pos)
		self.rotated_cutting_mask = pygame.mask.from_surface(self.rotated_cutting_surface)


class Mower01(Mower):
	def __init__(self):
		super().__init__("images/lawn_mower01.png", (0,0))