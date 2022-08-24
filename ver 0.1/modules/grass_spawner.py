import pygame
import random
from modules.grass import*

class GrassSpawner:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()
		self.width, self.height = self.display_surface.get_size()
		self.grass_list = []
		self.delay = 10
		self.delay_index = 0
		self.grass_amount = 3
		self.max_grass = 100
		self.lawn_mower = None

	def spawn_grass(self):
		if self.delay_index < self.delay:
			self.delay_index += 1
		elif len(self.grass_list) < self.max_grass:
			for i in range(self.grass_amount):
				grass = Grass()
				self.grass_list.append(grass)
				grass.spawn(random.randint(20, self.width-20), random.randint(20, self.height-20), self)
				self.delay_index = 0

	def remove_grass(self, grass):
		self.grass_list.remove(grass)

	def check_if_cut(self):
		for grass in self.grass_list:
			offset_x = self.lawn_mower.rect.center[0] - grass.x 
			offset_y = self.lawn_mower.rect.center[1] - grass.y
			if grass.mask.overlap(self.lawn_mower.mask, (offset_x, offset_y)) != None:
				grass.remove_self()

	def update(self, lawn_mower):
		self.check_if_cut()
		self.lawn_mower = lawn_mower
		self.spawn_grass()
		for i in self.grass_list:
			i.draw()

