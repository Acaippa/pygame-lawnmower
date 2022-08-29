import pygame
from random import*
from math import*

class Particle: # Particle moving in a certain direction at a certain speed for a certain time.
	def __init__(self, pos, angle, ttl, velocity, size, color, image = None):
		self.display_surface = pygame.display.get_surface()
		if image != None:
			self.image = image
		else:
			self.image = pygame.Surface((size, size))
			self.color = color
			self.image.fill(self.color)

		self.pos = pos

		self.angle = angle

		self.velocity = velocity # Pixels per second.

		self.time_to_live = ttl # The time the particle will be alive in seconds.

		self.time_alive = 0 # Time alive in seconds.

		self.delta_time = 0

	def update(self, dt):
		self.delta_time = dt

		self.pos = self.pos[0] - (self.velocity * cos(self.angle)) * self.delta_time, self.pos[1] - (self.velocity * sin(self.angle)) * self.delta_time

		self.draw()

	def draw(self):
		self.display_surface.blit(self.image, self.pos)

class ParticleSpawner:
	def __init__(self): # Spawns particles.
		self.display_surface = pygame.display.get_surface()

		self.delta_time = 0

		self.particle_list = []


	def update(self, dt):
		self.delta_time = dt

		self.update_particles()

	def draw(self):
		pass

	def spawn_particles(self, **kwargs):
		position = kwargs.get("pos", (0, 0))
		angle = kwargs.get("angle", 0)
		time_to_live = kwargs.get("ttl", 3)
		velocity = kwargs.get("velocity", 10)
		size = kwargs.get("size", 20)
		color = kwargs.get("color", "#ff0000")
		image = kwargs.get("image", None)

		self.particle_list.append(Particle(position, angle, time_to_live, velocity, size, color, image))

	def update_particles(self):
		for particle in self.particle_list:
			particle.update(self.delta_time)