from fanpy import sprite


class GFX:
	def __init__(self):
		self.layer_back_ground = sprite.Group()
		self.layer_food = sprite.Group()
		self.layer_snake_body = sprite.Group()
		self.layer_snake_head = sprite.Group()
		
		self.layers = [
			self.layer_back_ground,
			self.layer_food,
			self.layer_snake_body,
			self.layer_snake_head]
	
	def update(self):
		for layer in self.layers:
			layer.update()
	
	def render(self, display):
		for layer in self.layers:
			layer.draw(display)
