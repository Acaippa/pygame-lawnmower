import pygame
import math
from settings import*
from random import*
from modules.particles import*

class Mower(pygame.sprite.Sprite):
	def __init__(self, image, pos): # Abstract mower class.
		pygame.sprite.Sprite.__init__(self)
		self.display_surface = pygame.display.get_surface()

		self.image = pygame.image.load(image).convert_alpha()
		w, h = self.image.get_size()
		self.image = pygame.transform.scale(self.image, (w * MOWER_SIZE, h * MOWER_SIZE)) # Multiply the size of the mower according to settings.py.

		self.pos = pos

		self.delta_time = 0

		self.rect = self.image.get_rect(center=self.pos)

		self.angle = 0

		self.speed = 50

		self.turn_rate = 100

		self.cutting_surface = pygame.Surface((30, 40), pygame.SRCALPHA)
		self.cutting_surface.fill("#ffffff")

		self.rotated_cutting_surface = pygame.transform.rotate(self.cutting_surface, self.angle)
		self.rotated_cutting_surface_rect = self.rotated_cutting_surface.get_rect(center = self.pos)

		self.cutting_mask = pygame.mask.from_surface(self.rotated_cutting_surface)

		self.on_bool = True

		self.grass_particles = ParticleSpawner()

		self.particles_per_frame = 5

	def update(self, dt):
		self.delta_time = dt
		
		self.process_input()

		self.rotate()

		self.grass_particles.update(self.delta_time)

		self.draw()

	def draw(self):
		if self.on_bool: # Make the mower shake slightly when on
			self.display_surface.blit(self.rotated_image, (self.rect[0] + uniform(-1, 1) * self.delta_time, self.rect[1] + uniform(-1, 1) * self.delta_time))
		else:
			self.display_surface.blit(self.rotated_image, self.rect)

	def process_input(self):
		keys = pygame.key.get_pressed()

		radians = math.radians(self.angle)

		# Move the mower in self.angle or turn by increasing or decreasing self.angle.

		if keys[pygame.K_UP]:
			self.pos = self.pos[0] - (math.sin(radians) * self.speed) * self.delta_time, self.pos[1] - (math.cos(radians) * self.speed) * self.delta_time

		if keys[pygame.K_DOWN]:
			self.pos = self.pos[0] + (math.sin(radians) * self.speed) * self.delta_time, self.pos[1] + (math.cos(radians) * self.speed) * self.delta_time

		if keys[pygame.K_RIGHT]:
			self.angle -= self.turn_rate * self.delta_time

		if keys[pygame.K_LEFT]:
			self.angle += self.turn_rate * self.delta_time

	def rotate(self): # Rotate both the mower Surface and the cutting Surface and update their rects and masks.
		self.rotated_image = pygame.transform.rotate(self.image, self.angle)
		self.rect = self.rotated_image.get_rect(center=self.pos)

		self.rotated_cutting_surface = pygame.transform.rotate(self.cutting_surface, self.angle)
		self.rotated_cutting_surface_rect = self.rotated_cutting_surface.get_rect(center = self.pos)
		self.rotated_cutting_mask = pygame.mask.from_surface(self.rotated_cutting_surface)

	def on_collision(self):
		for i in range(self.particles_per_frame):
			self.grass_particles.spawn_particles(pos=self.pos, angle=radians(self.angle+100+uniform(-10, 10)), velocity=randint(400, 500), ttl=uniform(0.1, 0.2), color=choice(GRASS_COLORS_PARTICLES), size=5)



class Mower01(Mower):
	def __init__(self):
		super().__init__("images/lawn_mower01.png", (0,0))