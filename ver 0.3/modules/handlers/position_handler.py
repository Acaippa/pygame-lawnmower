
class PH:
	def __init__(self, item):
		self.item = item

	def parse_pos(self, **kwargs):
		pos = self.item.pos

		margin = kwargs.get("margin", 0)

		w, h = self.item.display_surface.get_size()

		try:
			if self.item.container != None:
				w, h = self.item.container.size
		except:
			pass

		if self.item.pos[0] == "center":
			self.item.pos = w / 2 - self.item.surface.get_width() / 2, self.item.pos[1]

		if self.item.pos[1] == "center":
			self.item.pos = self.item.pos[0], h / 2 - self.item.surface.get_height() / 2

		if self.item.pos[1] == "top":
			self.item.pos = self.item.pos[0], 0 + self.item.surface.get_height() + margin

		if self.item.pos[1] == "bottom":
			self.item.pos = self.item.pos[0], h - self.item.surface.get_height() - margin

		if self.item.pos[0] == "right":
			self.item.pos = w - self.item.surface.get_width() - margin

		if self.item.pos[0] == "left":
			self.item.pos = 0 + self.item.surface.get_width() + margin