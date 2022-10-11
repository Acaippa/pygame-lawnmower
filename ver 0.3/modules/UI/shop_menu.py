import pygame
from math import*
from modules.UI.container import *
from modules.UI.button import *

class ShopMenu:
	def __init__(self, parent, **kwargs):
		self.parent = parent

		self.display_surface = self.parent.surface

		self.surface = pygame.Surface((400, 500))

		self.background_color = kwargs.get("background", "#3f3f3f")

		self.surface.fill(self.background_color)

		self.surface_w, self.surface_h = self.surface.get_size()

		self.display_w, self.display_h = self.display_surface.get_size()

		self.pos = kwargs.get("pos", (self.display_w / 2 - self.surface.get_width() / 2, - self.surface_h))

		self.item_list = []

		self.delta_time = 0

		self.destination = self.pos

		self.shown = False

		self.main_container = Container(self, size=self.surface.get_size(), align="centerx", direction="bottom")

		self.section_container = Container(self, container=self.main_container, size=(self.main_container.size[0], 70), align="left", direction="right", padding=30, padding_between=40)

		self.mower_button = Button(self, container=self.section_container, text="Mowers")
		self.mower_button = Button(self, container=self.section_container, text="Bags")

		self.mower_section = Container(self, container=self.main_container, padding=20, align="left", direction="right")
		self.mower_button = Button(self, container=self.mower_section, text="Bags")
		self.mower_button = Button(self, container=self.mower_section, text="Bags")

	def update(self, dt):
		self.delta_time = dt
		self.draw_background()

		self.move()

		self.update_items()

		self.draw()

	def draw(self):
		self.display_surface.blit(self.surface, self.pos)

	def move(self, speed=1000, range=10):
		if self.pos != self.destination:
			if self.destination[0] > self.pos[0]: 
				self.pos = self.pos[0] + speed * self.delta_time, self.pos[1] # If X is greater
			elif self.destination[0] < self.pos[0]: 
				self.pos = self.pos[0] - speed * self.delta_time, self.pos[1] # If X is smaller

			if self.destination[1] > self.pos[1]:
				self.pos = self.pos[0], self.pos[1] + speed * self.delta_time # If Y is greater
			elif self.destination[1] < self.pos[1]:
				self.pos = self.pos[0], self.pos[1] - speed * self.delta_time # If Y is smaller

		# If the curent position is close enough to its destination, snap the menu into place so it doesnt oscillate.
		if hypot(self.pos[0]-self.destination[0], self.pos[1]-self.destination[1]) < range:
			self.pos = self.destination

	def toggle(self):
		if self.shown:
			self.destination = self.pos[0], - self.surface_h
			self.shown = False
		else:
			self.destination = self.pos[0], 100
			self.shown = True

	def update_items(self):
		for item in self.item_list:
			item.update(self.delta_time)

	def draw_background(self):
		self.surface.fill(self.background_color)

