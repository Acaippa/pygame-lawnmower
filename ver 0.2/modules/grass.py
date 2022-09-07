import pygame
from settings import*
from random import*

class Grass(pygame.sprite.Sprite):
	def __init__(self, pos, spawner):
		pygame.sprite.Sprite.__init__(self)
		self.display_surface = pygame.display.get_surface()
		self.image = pygame.Surface((0, 0))

		self.color_list = GRASS_COLORS

		self.color = self.get_color()

		self.image.fill(self.get_color()) # Make the grass a random color from the self.color_list.

		self.delta_time = 0

		self.pos = pos

		self.spawner = spawner

		self.size = 0

		self.grow_bool = True

		self.mask = pygame.mask.from_surface(self.image)

		self.rect = self.image.get_rect(center = self.pos)

		self.blit_pos = (self.pos[0] - self.image.get_width() // 2, self.pos[1] - self.image.get_height() // 2)

	def update(self, dt):
		self.delta_time = dt
		
		# Only run when growing to save on resources.
		if self.grow_bool:
			self.blit_pos = (self.pos[0] - self.image.get_width() // 2, self.pos[1] - self.image.get_height() // 2)
			self.grow()

		self.draw()

	def draw(self):
		self.display_surface.blit(self.image, self.blit_pos)

	def grow(self): # Make the grass bigger and update mask.
		if self.size + GROW_RATE * self.delta_time < GRASS_SIZE:
			self.size += GROW_RATE * self.delta_time
			self.mask = pygame.mask.from_surface(self.image)
			self.image = pygame.Surface((self.size, self.size))
			self.image.fill(self.color)
			self.rect = self.image.get_rect(center = self.pos)
		else:
			self.grow_bool = False		

	def get_color(self):
		return choice(self.color_list)

	def on_collision(self, parent):
		parent.grass_list.remove(self)