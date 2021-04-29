import pygame
from pygame.math import Vector2
from constants import CELL_SIZE, CELLS_TOTAL
from ultracolors import GOLD
from random import randint


class Fruit:
	def __init__(self):
		self.pos = self.create_new_position()
	
	def draw_fruit(self, display):
		rect = pygame.Rect(
			self.pos.x * CELL_SIZE,
			self.pos.y * CELL_SIZE,
			CELL_SIZE,
			CELL_SIZE
		)
		pygame.draw.rect(surface=display, color=GOLD, rect=rect)
		
	@staticmethod
	def create_new_position() -> Vector2:
		x = randint(0, CELLS_TOTAL-1)
		y = randint(0, CELLS_TOTAL-1)
		return Vector2(x, y)
