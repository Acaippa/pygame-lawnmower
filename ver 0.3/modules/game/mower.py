import pygame
from math import* 
from random import *

class Mower:
	def __init__(self, parent, **kwargs):
		self.parent = parent

		self.display_surface = self.parent.parent.surface

		self.dict = kwargs.get("dict", None)

		self.speed = self.dict["speed"]

		self.image_path = self.dict["image"]

		self.turn_rate = self.dict["turn_rate"]

		self.margin = self.dict["margin"] # The margin between the image size and the cutting surface size.

		self.size = self.dict["size"]

		self.body_width, self.body_length = self.dict["body_width"], self.dict["body_length"]

		self.image = pygame.image.load(self.image_path).convert_alpha()

		self.old_image_size = self.image.get_size()

		self.angle = 0

		self.pos = (20, 20)


		self.image = pygame.transform.scale(self.image, self.size)
		self.rect = self.image.get_rect(center=self.pos)

		self.image_size_increase = self.image.get_size()[0] / self.old_image_size[0], self.image.get_size()[1] / self.old_image_size[1]

		self.shaking = True

		self.delta_time = 0

		w, h = self.image.get_size()

		self.cutting_surface = pygame.Surface(((self.body_width * self.image_size_increase[0] - self.margin), (self.body_width * self.image_size_increase[1]) - self.margin), pygame.SRCALPHA)
		self.cutting_surface.fill("white")
		self.cutting_mask = pygame.mask.from_surface(self.cutting_surface)

		self.cutting_rect = self.cutting_surface.get_rect()

		self.grass_list = []

	def update(self, dt):
		self.delta_time = dt

		self.input()

		self.cut_grass()

		self.draw()

	def draw(self):
		self.rotated_image = pygame.transform.rotate(self.image, self.angle)
		self.rotated_cutting_surface = pygame.transform.rotate(self.cutting_surface, self.angle)
		self.cutting_mask = pygame.mask.from_surface(self.rotated_cutting_surface)

		self.rect = self.rotated_image.get_rect(center=self.pos)
		self.cutting_rect = self.rotated_cutting_surface.get_rect(center=self.pos)

		self.display_surface.blit(self.rotated_image, ((self.rect[0] - 1 * sin(radians(randint(0, 360)))), self.rect[1] - 1 * cos(radians(randint(0, 360)))))

	def input(self):
		rads = radians(self.angle)
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			self.pos = self.pos[0] - (self.speed*sin(rads)) * self.delta_time, self.pos[1] - (self.speed*cos(rads)) * self.delta_time

		if keys[pygame.K_DOWN]:
			self.pos = self.pos[0] + (self.speed*sin(rads)) * self.delta_time, self.pos[1] + (self.speed*cos(rads)) * self.delta_time

		if keys[pygame.K_RIGHT]:
			self.angle -= self.turn_rate * self.delta_time

		if keys[pygame.K_LEFT]:
			self.angle += self.turn_rate * self.delta_time

	def cut_grass(self):
		for grass in self.grass_list:
			offset_x, offset_y = self.pos[0] - (grass.rect[0] + grass.parent.parent.pos[0]), (self.pos[1] + self.body_length) - (grass.rect[1] + grass.parent.parent.pos[1])

			if self.cutting_mask.overlap(grass.mask, (offset_x, offset_y)) != None:
				grass.remove_self()
