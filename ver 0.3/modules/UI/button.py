import pygame
from .text import*

class Button(Text):
	def __init__(self, parent, **kwargs):
		super().__init__(parent, **kwargs)

		self.padding = kwargs.get("padding", 15)

		self.margin = kwargs.get("margin", 0)

		self.background_color = kwargs.get("background", "#2f2f2f")

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

		# In order to detect the collision of the cursor to the rect of the button even if its on a surface, we have to subtract the position of the surface to get the "real" position of the button
		try:
			mouse_pos = mouse_pos[0] - self.parent.pos[0], mouse_pos[1] - self.parent.pos[1]
		except:
			pass

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

	def update_pos(self):
		w, h = self.display_surface.get_size() if self.container == None else self.container.size

		if self.pos[0] == "center":
			self.pos = w / 2 - self.image.get_width() / 2, self.pos[1]

		if self.pos[1] == "center":
			self.pos = self.pos[0], h / 2 - self.image.get_height() / 2

		if self.pos[0] == "right":
			self.pos = w - (self.padding * 5) / 2 - self.margin, self.pos[1]

		if self.pos[0] == "left":
			self.pos = 0 + (self.padding * 5) / 2 + self.margin, self.pos[1]

		if self.pos[1] == "top":
			self.pos = self.pos[0], 0 + (self.padding * 2) / 2 + self.margin

		if self.pos[1] == "bottom":
			self.pos = self.pos[1], h - self.image.get_height() - self.margin



