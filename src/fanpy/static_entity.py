from fanpy import Surface, sprite
from constants import BOX, GREEN


class StaticEntity(sprite.Sprite):
	def __init__(self, image=Surface(BOX), color=GREEN):
		super(StaticEntity, self).__init__()
		self.image = image
		self.rect = self.image.get_rect()
		self.image.fill(color)
		self.vel_x = 0
		self.vel_y = 0
	
	def update(self, *args, **kwargs):
		self.update_pos()
		
	def update_pos(self):
		self.rect.x += self.vel_x
		self.rect.y += self.vel_y
