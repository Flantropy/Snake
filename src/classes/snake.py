import pygame
from pygame.math import Vector2
from constants import CELL_SIZE
from ultracolors import DARK_OLIVE_GREEN


class Snake:
	def __init__(self):
		self.body = [Vector2(9, 9), Vector2(10, 9), Vector2(11, 9)]
		self.color = DARK_OLIVE_GREEN
		self.__direction = Vector2(-1, 0)
		self.block_to_add = False
	
	@property
	def direction(self):
		return self.__direction
	
	@direction.setter
	def direction(self, v2: Vector2):
		if self.__direction.x + v2.x != 0:
			self.__direction = v2
	
	def draw_snake(self, display):
		for cell in self.body:
			x_pos = cell.x * CELL_SIZE
			y_pos = cell.y * CELL_SIZE
			cell_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
			pygame.draw.rect(surface=display, color=self.color, rect=cell_rect)
	
	def move_snake(self):
		flag = None if self.block_to_add else -1
		body_copy = self.body[:flag]
		body_copy.insert(0, body_copy[0] + self.direction)
		self.body = body_copy[:]
		self.block_to_add = False
