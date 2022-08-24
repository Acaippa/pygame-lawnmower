import pygame 

class Grass(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.image = pygame.image.load("images/grass.png").convert_alpha()
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()
		self.size = 0
		self.max_size = 20
		self.spawner = None

	def spawn(self, x, y, spawner):
		self.x, self.y = x, y
		self.spawner = spawner

	def remove_self(self):
		self.spawner.remove_grass(self)

	def draw(self):
		if self.size < self.max_size:
			self.size += 1
		self.image = pygame.transform.scale(self.image, (self.size, self.size))
		self.rect = self.image.get_rect()
		self.display_surface.blit(self.image, (self.x-self.size//2, self.y-self.size//2)) # Draw the rect at the center instead of at the corner
