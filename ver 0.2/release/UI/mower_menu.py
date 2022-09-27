import pygame
from modules.mower import*
from UI.container import*
from UI.image import*

class MowerMenu:
	def __init__(self, level):
		self.display_surface = pygame.display.get_surface()

		self.delta_time = 0

		self.level = level

		self.mower_list = [
			Mower01(self.level),
			Mower02(self.level)
		]

		self.margin = 30

		self.width = 200

		self.pos = (-self.width, self.margin)

		w, h = self.display_surface.get_size()
		self.surface = pygame.Surface((self.width, h - self.margin * 2))

		self.background_color = "#1A1A1A"

		self.surface.fill(self.background_color)

		self.velocity = 500

		self.hide_self_bool = True
		self.show_self_bool = False

		self.hidden = True

		self.item_list = [] # The items inside the main_container will be placed here.

		self.main_container = Container(surface=self.surface, overflow=2, padding=10)
		

	def update(self, dt):
		self.delta_time = dt

		self.draw_items()

		self.move()

		self.draw()

		self.main_container.update(self.delta_time)

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

	def draw_items(self):
		# Clear the item list to prevent lag.
		self.main_container.item_list.clear()

		for mower in self.mower_list:
			container = Container(container=self.main_container, background="#3f3f3f", overflow=1)
			image = Image(container = container, image = mower.image_path, adapt=True)
			mouse = pygame.mouse.get_pos()

