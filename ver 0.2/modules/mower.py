import pygame
import math
from settings import*
from random import*
from modules.particles import*


class Mower(pygame.sprite.Sprite):
	def __init__(self, image, pos, **kwargs): # Abstract mower class.
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

		self.grass_cut = 0

		self.shaking_offset = (0, 0)

		bag_image = kwargs.get("bag", None)

		if bag_image != None:
			self.bag = Bag(self, bag_image[0], bag_image[1])

	def update(self, dt):
		self.delta_time = dt
		
		self.process_input()

		self.rotate()

		if self.bag != None:
			self.bag.update(self.delta_time)

		self.grass_particles.update(self.delta_time)

		self.draw()

	def draw(self):
		if self.on_bool: # Make the mower shake slightly when on
			self.shaking_offset = (uniform(-1, 1) * self.delta_time, uniform(-1, 1) * self.delta_time)
			self.display_surface.blit(self.rotated_image, (self.rect[0] + self.shaking_offset[0], self.rect[1] + self.shaking_offset[1]))
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
		self.fill_bag()

	def fill_bag(self):
		if self.bag.capacity_index != self.bag.capacity:
			self.bag.capacity_index += 1
		
			for i in range(self.particles_per_frame):
				self.grass_particles.spawn_particles(pos=self.pos, angle=radians(self.angle-90 +uniform(-10, 10)), velocity=randint(400, 500), ttl=uniform(0.1, 0.2), color=choice(GRASS_COLORS_PARTICLES), size=5)

	def get_grass_cut(self):
		return self.grass_cut


class Bag:
	def __init__(self, mower, image, drag_image):
		self.display_surface = pygame.display.get_surface()

		self.mower = mower

		self.delta_time = 0

		self.image_path = image

		self.image = pygame.image.load(image)
		w, h = self.image.get_size()


		self.image = pygame.transform.scale(self.image, (w * MOWER_SIZE, h * MOWER_SIZE))
		self.image = pygame.transform.rotate(self.image, self.mower.angle)
		self.rect = self.image.get_rect()

		self.drag_image = pygame.image.load(drag_image)
		w, h = self.drag_image.get_size()

		self.drag_image = pygame.transform.scale(self.drag_image, (w * MOWER_SIZE, h * MOWER_SIZE))
		self.drag_image_rotated = pygame.transform.rotate(self.drag_image, self.mower.angle)
		self.drag_rect = self.drag_image.get_rect()

		self.attached_to_mower = True

		self.capacity = 100
		self.capacity_index = 0 # The grass in the bag.

	def update(self, dt):
		self.delta_time = dt

		self.move_self()

		self.check_if_dragging()

		self.draw()

	def draw(self):
		if self.attached_to_mower:
			self.display_surface.blit(self.image_rotated, self.pos)
		else:
			self.drag_image_rotated = pygame.transform.rotate(self.drag_image, self.mower.angle)
			self.display_surface.blit(self.drag_image_rotated, self.pos)


	def move_self(self):
		if self.attached_to_mower:
			self.image_rotated = pygame.transform.rotate(self.image, self.mower.angle)
			self.rect = self.image.get_rect(center=self.mower.rect.center)
			self.mask = pygame.mask.from_surface(self.image_rotated)
			self.pos = (self.mower.rect[0] + self.mower.shaking_offset[0], self.mower.rect[1] + self.mower.shaking_offset[1])

		if self.attached_to_mower == False:
			mouse_pos = pygame.mouse.get_pos()
			self.pos = mouse_pos[0] - self.drag_image_rotated.get_width() // 2, mouse_pos[1] - self.drag_image_rotated.get_height() // 2

	def check_if_dragging(self):
		mouse_pos = pygame.mouse.get_pos()
		mouse_clicked = pygame.mouse.get_pressed()

		if mouse_clicked[0] == False:
			# Update the position to be the mower when the user lets go of the bag to prevent the bag from flashing when letting go.
			self.pos = (self.mower.rect[0] + self.mower.shaking_offset[0], self.mower.rect[1] + self.mower.shaking_offset[1])
			self.attached_to_mower = True

		try:
			if self.mask.get_at((mouse_pos[0] - self.mower.rect[0], mouse_pos[1] - self.mower.rect[1])) != 0 and mouse_clicked[0]:
				self.attached_to_mower = False
		except Exception as e:
			print(e)


class Mower01(Mower):
	def __init__(self):
		super().__init__("images/lawn_mower01.png", (0,0), bag=("images/mower_bag01.png", "images/mower_bag01drag.png"))