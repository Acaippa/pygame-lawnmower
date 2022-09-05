import pygame
from modules.mower import*

class MowerMenu:
	def __init__(self, level):
		self.display_surface = pygame.display.get_surface()

		self.delta_time = 0

		self.level = level

		self.mower_list = [
			Mower01(self.level)
		]

		self.margin = 30

		self.width = 200

		self.pos = (0, self.margin)

		w, h = self.display_surface.get_size()
		self.surface = pygame.Surface((self.width, h - self.margin * 2))

		self.velocity = 500

		self.hide_self_bool = False
		self.show_self_bool = True

		self.hidden = True

	def update(self, dt):
		self.delta_time = dt

		self.move()

		self.draw()

	def draw(self):
		self.display_surface.blit(self.surface, self.pos)

	def move(self):
		if self.hide_self_bool:
			if self.pos[0] > -self.width:
				self.pos = self.pos[0] - self.velocity * self.delta_time, self.pos[1]
			else:
				self.hide_self_bool = False
				self.hidden = False

		if self.show_self_bool:
			if self.pos[0] < 0:
				self.pos = self.pos[0] + self.velocity * self.delta_time, self.pos[1]
			else:
				self.show_self_bool = False
				self.hidden = True
				self.pos = 0, self.pos[1]

	def hide_self(self):
		self.hide_self_bool = True

	def show_self(self):
		self.show_self_bool = True

	def toggle(self):
		if self.hidden:
			self.hide_self()

		if not self.hidden:
			self.show_self()