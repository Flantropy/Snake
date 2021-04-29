import sys
import pygame
from classes.fruit import Fruit
from classes.snake import Snake
from constants import CELLS_TOTAL


class Game:
	def __init__(self):
		self.snake = Snake()
		self.fruit = Fruit()
	
	def update(self):
		self.check_collision()
		self.snake.move_snake()
		self.check_game_over()
		self.check_screen_crossed()
	
	def draw_elements(self, display):
		self.fruit.draw_fruit(display)
		self.snake.draw_snake(display)
	
	def check_collision(self):
		if self.fruit.pos == self.snake.body[0]:
			self.fruit.pos = self.fruit.create_new_position()
			self.snake.block_to_add = True
	
	def check_screen_crossed(self):
		if self.snake.body[0].x < 0:
			self.snake.body[0].x = CELLS_TOTAL - 1
		if self.snake.body[0].x == CELLS_TOTAL:
			self.snake.body[0].x = 0
		if self.snake.body[0].y < 0:
			self.snake.body[0].y = CELLS_TOTAL - 1
		if self.snake.body[0].y == CELLS_TOTAL:
			self.snake.body[0].y = 0

	def check_game_over(self):
		if self.snake.body[0] in self.snake.body[1:]:
			print('sake bite itself')
			self.close_game()
	
	@staticmethod
	def close_game():
		pygame.quit()
		sys.exit()
