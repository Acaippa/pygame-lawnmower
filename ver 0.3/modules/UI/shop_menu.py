import pygame
from math import*
from modules.UI.container import *
from modules.UI.button import *
from modules.UI.image import *
from modules.settings.json_manager import *
from modules.game.mower import *
from modules.game.bag import *
import json

class ShopMenu:
	def __init__(self, parent, **kwargs):
		self.parent = parent

		self.display_surface = self.parent.surface

		self.surface = pygame.Surface((370, 500))

		self.background_color = kwargs.get("background", "#3f3f3f")

		self.surface.fill(self.background_color)

		self.surface_w, self.surface_h = self.surface.get_size()

		self.display_w, self.display_h = self.display_surface.get_size()

		self.pos = kwargs.get("pos", (self.display_w / 2 - self.surface.get_width() / 2, - self.surface_h))

		self.item_list = []

		self.delta_time = 0

		self.destination = self.pos

		self.shown = False

		self.mowers = Load("modules/game/mowers.json")["mowers"]
		self.bags = Load("modules/game/bags.json")["bags"]

		self.main_container = Container(self, size=self.surface.get_size(), align="centerx", direction="bottom", padding=15)

		self.section_container = Container(self, container=self.main_container, size=(self.main_container.size[0], 70), align="left", direction="right", padding_between=10)
		self.mower_button = Button(self, container=self.section_container, text="Mowers", command=self.activate_mower_section)
		self.bag_button = Button(self, container=self.section_container, text="Bags", command=self.activate_bag_section)

		self.mower_section = Container(self, container=self.main_container, align="left", direction="right", size=(self.main_container.size[0], self.main_container.size[1]-self.section_container.size[1]), padding_between=20, halt=True)
		self.bag_section = Container(self, container=self.main_container, align="left", direction="right", size=(self.main_container.size[0], self.main_container.size[1]-self.section_container.size[1]), padding_between=20, halt=True)
		self.bag_section.halt = True

		self.mower_dict = {}
		self.bag_dict = {}
		self.container_dict = {}

		print(len(self.mowers))

		for index, mower in enumerate(self.mowers):
			self.mower_dict[index] = mower

			container = Container(self, container=self.mower_section, background="#2f2f2f", padding=5, align="left", direction="bottom", size=(110, 130), command=lambda index = index: self.change_mower(index))
			Image(self, container=container, image=mower["image"], size=(container.size[0] - 10, container.size[1] - 30))
			Text(self, container=container, text=str(mower["price"]))

		for index, bag in enumerate(self.bags):
			self.bag_dict[index] = bag

			container = Container(self, container=self.bag_section, background="#2f2f2f", padding=5, align="left", direction="bottom", size=(110, 130))
			Image(self, container=container, image=bag["image"], size=(container.size[0] - 10, container.size[1] - 30))
			Text(self, container=container, text=str(bag["price"]))			

		self.change_mower(1)



	def update(self, dt):
		self.delta_time = dt
		self.draw_background()

		self.move()

		self.update_items()

		self.current_mower.update(self.delta_time)
		self.current_bag.update(self.delta_time)

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

	def activate_mower_section(self):
		self.mower_section.halt = False
		self.bag_section.halt = True

	def activate_bag_section(self):
		self.mower_section.halt = True
		self.bag_section.halt = False

	def change_mower(self, index):
		self.current_mower = Mower(self, dict=self.mower_dict[index])
		self.current_bag = Bag(self, dict=self.bag_dict[0], mower=self.current_mower)
		self.current_bag.mower = self.current_mower

		self.parent.current_mower = self.current_mower
		self.parent.current_bag = self.current_bag



