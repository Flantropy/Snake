from fanpy import DynamicEntity, sprite, StaticEntity
from random import choice, randrange
from constants import BOX_SIDE, DISPLAY_WIDTH, DISPLAY_HEIGHT, WHITE, GREEN, BLUE
from typing import NamedTuple


class V2(NamedTuple):
	horizontal_speed: int
	vertical_speed: int
	
		
class Snake(DynamicEntity):
	def __init__(self):
		super(Snake, self).__init__()
		self.directions = dict(
			up=V2(horizontal_speed=0, vertical_speed=-BOX_SIDE),
			down=V2(horizontal_speed=0, vertical_speed=BOX_SIDE),
			left=V2(horizontal_speed=-BOX_SIDE, vertical_speed=0),
			right=V2(horizontal_speed=BOX_SIDE, vertical_speed=0)
		)

		self.direction = "up"
		self.rect.x = randrange(0, DISPLAY_WIDTH, BOX_SIDE)
		self.rect.y = randrange(0, DISPLAY_HEIGHT, BOX_SIDE)
		self.turn(choice(list(self.directions.keys())))
		self.body = list()
	
	def update(self):
		super().update()
		self.check_if_cross_screen_bounds()
	
	def change_speed(self):
		self.vel_x, self.vel_y = self.directions[self.direction]
	
	def turn(self, new_direction: str):
		current_v2 = self.directions[self.direction]
		if current_v2.horizontal_speed + self.directions[new_direction].horizontal_speed != 0:
			self.direction = new_direction
			self.change_speed()
	
	def eat(self, food):
		pass
	
	def check_if_cross_screen_bounds(self):
		if self.rect.x >= DISPLAY_WIDTH:
			self.rect.x = 0
		if self.rect.x < 0:
			self.rect.x = DISPLAY_WIDTH - BOX_SIDE
		if self.rect.y >= DISPLAY_HEIGHT:
			self.rect.y = 0
		if self.rect.y < 0:
			self.rect.y = DISPLAY_WIDTH - BOX_SIDE
