import pygame
from .text import*

class Button(Text):
	def __init__(self, parent, **kwargs):
		super().__init__(parent, **kwargs)

		self.padding = kwargs.get("padding", 15)

		self.background_color = kwargs.get("background_color", "#2f2f2f")

		self.background_color_hover = kwargs.get("hover_color", "#4f4f4f")

		self.background_color_click = kwargs.get("click_color", "5f5f5f")

		self.background_color_current = self.background_color

		self.click_check = False

		self.command = kwargs.get("command", self.fallback_command)

		self.cmd_list.extend([self.draw_background, self.on_hover])

	def draw_background(self):
		self.rect.width += self.padding * 5
		self.rect.height += self.padding * 2

		self.rect[0] -= self.padding * 2.5
		self.rect[1] -= self.padding

		pygame.draw.rect(self.display_surface, self.background_color_current, self.rect, border_radius=0)

	def on_hover(self):
		mouse_pos = pygame.mouse.get_pos()
		mouse_clicked = pygame.mouse.get_pressed()

		if self.rect.collidepoint(mouse_pos):
			self.background_color_current = self.background_color_hover
		else:
			self.background_color_current = self.background_color

		if self.rect.collidepoint(mouse_pos) and mouse_clicked[0] == True: # Check if the user clicks the button
			self.click_check = True

		if self.rect.collidepoint(mouse_pos) and mouse_clicked[0] == False and self.click_check: # Check if the user released the button while inside the button
			self.command()
			self.click_check = False

		if not self.rect.collidepoint(mouse_pos): # Check if the user left the button after clicking
			self.click_check = False

	def fallback_command(self):
		print(f"Button {__name__} Has no function yet.")



