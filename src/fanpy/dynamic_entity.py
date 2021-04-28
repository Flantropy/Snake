from fanpy.static_entity import StaticEntity
from fanpy import Surface
from constants import BOX, RED


class DynamicEntity(StaticEntity):
	def __init__(self, image=Surface(BOX)):
		super(DynamicEntity, self).__init__(image=image)
		self.color = RED
		self.image.fill(RED)
	
	def update(self):
		self.update_pos()
