import pygame
from random import randrange

from constants import *
from fanpy import EventHandler, GFX, StaticEntity, Surface, sprite
from classes.snake import Snake
from classes.food import Food


class MainScene(object):
	def __init__(self):
		pygame.init()
		self.display = pygame.display.set_mode(DISPLAY_SIZE)
		self.clock = pygame.time.Clock()
		self.event_handler = EventHandler()
		self.gfx = GFX()
		self.snake = None
	
	def run(self):
		self.__create_back_ground()
		self.__generate_food()
		self.__create_snake()
		while True:
			#  HANDLE EVENTS
			self.event_handler.handle_events(self.snake)
			
			# UPDATE AND RENDER
			if sprite.spritecollide(self.snake, self.gfx.layer_food, dokill=True):
				self.snake.eat()
			self.gfx.update()
			self.gfx.render(self.display)
			pygame.display.update()
			
			# TICK
			self.clock.tick(FPS)
	
	def __create_snake(self):
		self.snake = Snake()
		self.gfx.layer_snake_head.add(self.snake)
	
	def __generate_food(self):
		new_food = Food()
		new_food.image.fill(WHITE)
		new_food.rect.x = randrange(0, DISPLAY_WIDTH, BOX_SIDE)
		new_food.rect.y = randrange(0, DISPLAY_HEIGHT, BOX_SIDE)
		self.gfx.layer_food.add(new_food)
	
	def __create_back_ground(self):
		back_ground = StaticEntity(image=Surface(DISPLAY_SIZE))
		back_ground.image.fill(BLACK)
		self.gfx.layer_back_ground.add(back_ground)
