import pygame

class Mower:
	def __init__(self, parent, **kwargs):
		self.parent = parent

		self.display_surface = self.parent.surface

		self.dict = kwargs.get("dict", None)

		# self.speed = self.dict["speed"]

		# self.image_path = self.dict["image"]

		# self.margin = self.dict["margin"] # The margin between the image size and the cutting surface size.

		print(self.dict)

		self.delta_time = 0

	def update(self, dt):
		self.delta_time = dt

		self.draw()

	def draw(self):
		pass