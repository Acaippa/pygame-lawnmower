import pygame
from modules.ground import*
from modules.mower import*
from UI.player_info import*
from modules.composter import*
from modules.button import*
from UI.mower_menu import*

class LvlNormal:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()
		w, h = self.display_surface.get_size()

		self.delta_time = 0

		self.ground = Ground()

		self.test_mower = Mower01(self)

		self.player_info = PlayerInfo(self)

		self.composter = Composter(self.test_mower)

		self.mower_menu = MowerMenu(self)

		self.shop_button = Button(text="Shop", pos=("l", "b"), padding=7, margin=20, command=self.mower_menu.toggle)

		self.money = 0

	def update(self, dt):
		self.delta_time = dt

		self.ground.update(self.delta_time, self.test_mower)

		self.composter.update(self.delta_time)

		self.test_mower.update(self.delta_time)

		self.player_info.update(self.delta_time)

		self.mower_menu.update(self.delta_time)

		self.shop_button.update(self.delta_time)
		
		self.draw()

	def draw(self):
		pass