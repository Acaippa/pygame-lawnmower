import pygame

class Button:
	def __init__(self, **kwargs):
		self.display_surface = pygame.display.get_surface()
		pygame.font.init()

		self.pos = kwargs.get("pos", (0, 0))

		self.text = kwargs.get("text", "Lorem Ipsum")

		self.padding = kwargs.get("padding", 0)

		self.margin = kwargs.get("margin", 0)

		self.font = pygame.font.Font(None, 40)
		self.rendered_font = self.font.render(str(self.text), True, "#ffffff")
		self.rect = self.rendered_font.get_rect()

		self.image_path = kwargs.get("image", None)

		if self.image_path != None:
			self.image = pygame.image.load(self.image_path).convert_alpha()
			self.rect = self.image.get_rect()

		self.image_or_text = None

		self.delta_time = 0

		self.background_color = "#222222"

		self.command = kwargs.get("command", None)

		self.click_check = False

	def update(self, dt):
		self.delta_time = dt

		self.adjust()

		self.get_rect()

		self.on_hover()

		self.on_click()

		self.draw()

	def draw(self):
		if self.image_or_text == "image": # Image enabled.
			self.display_surface.blit(self.image, self.pos)

		else:
			pygame.draw.rect(self.display_surface, self.background_color, self.rect, border_radius=5) # Text enabled.
			self.display_surface.blit(self.rendered_font, (self.pos[0] - self.rendered_font.get_width() / 2, self.pos[1] - self.rendered_font.get_height() / 2))

	def get_rect(self):
		if self.image_path != None and self.text == "Lorem Ipsum": # Image enabled.
			self.rect = self.image_path.get_rect(center=self.pos)
			self.image_or_text = "image"

		if self.image_path == None and self.text != "Lorem Ipsum": # Text enabled.
			self.rendered_font = self.font.render(str(self.text), True, "#ffffff")
			self.rect = self.rendered_font.get_rect(center=self.pos)
			self.image_or_text = "text"

		self.rect.width += self.padding * 2
		self.rect.height += self.padding
		self.rect.center = self.pos

	def adjust(self):
		if self.pos[0] == "r":
			self.pos = self.display_surface.get_width() - self.rect.width // 2 - self.margin, self.pos[1]

		if self.pos[0] == "l":
			self.pos = 0 + self.rect.width // 2 + self.margin, self.pos[1]

		if self.pos[1] == "b":
			self.pos = self.pos[0], self.display_surface.get_height() - self.rect.height // 2 - self.margin

		if self.pos[1] == "t":
			self.pos = self.pos[0], 0 + self.rect.height // 2 + self.margin

	def on_hover(self):
		mouse_pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(mouse_pos):
			self.background_color = "#434343"
		else:
			self.background_color = "#222222"

	def on_click(self):
		mouse_pos = pygame.mouse.get_pos()
		mouse_clicked = pygame.mouse.get_pressed()

		if self.rect.collidepoint(mouse_pos) and mouse_clicked[0]:
			self.click_check = True
			self.background_color = "#565656"

		if self.rect.collidepoint(mouse_pos) and mouse_clicked[0] == False and self.click_check == True:
			self.command()
			self.click_check = False
