import pygame
from math import*

class EventHandler:
	def __init__(self):
		self.mower = None

		self.grass = []

		self.frame_amount = 10
		self.frame_index = 0

		self.close_grass = []

	def update(self, mower, grass):
		self.mower = mower

		self.grass = grass

		self.cut_grass()

	def cut_grass(self):
		# if self.frame_index >= self.frame_amount:
		# 	self.close_grass = []
		# 	for grass in self.grass:
		# 		dist = sqrt((self.mower.pos[0] - grass.pos[0])**2 + (self.mower.pos[1] - grass.pos[1])**2)
		# 		if dist < 20:
		# 			self.close_grass.append(grass)

		# 	self.frame_index = 0
		# else:
		# 	self.frame_index += 1

		# for grass in self.grass:
		# 	if sqrt((self.mower.pos[0] - grass.pos[0])**2 + (self.mower.pos[1] - grass.pos[1])**2) < 30:
		# 		offset_x = grass.rect[0] - self.mower.rotated_cutting_surface_rect[0]
		# 		offset_y = grass.rect[1] - self.mower.rotated_cutting_surface_rect[1]
		# 		if self.mower.rotated_cutting_mask.overlap(grass.mask, (offset_x, offset_y)) != None:
		# 			grass.on_collision()
		
