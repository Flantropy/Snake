import sys
import pygame
from pygame.math import Vector2

from constants import *
from classes.game import Game
from ultracolors import BLACK


class MainScene:
	def __init__(self):
		pygame.init()
		self.game = Game()
		self.display = pygame.display.set_mode(DISPLAY_SIZE)
		self.clock = pygame.time.Clock()
		self.update_game = pygame.USEREVENT
		pygame.time.set_timer(self.update_game, GAME_SPEED)
	
	def run(self):
		while True:
			#  HANDLE EVENTS
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.game.close_game()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						self.game.snake.direction = Vector2(0, -1)
					elif event.key == pygame.K_DOWN:
						self.game.snake.direction = Vector2(0, 1)
					elif event.key == pygame.K_RIGHT:
						self.game.snake.direction = Vector2(1, 0)
					elif event.key == pygame.K_LEFT:
						self.game.snake.direction = Vector2(-1, 0)
				if event.type == self.update_game:
					self.game.update()
					
			# RENDER
			self.display.fill(BLACK)
			self.game.draw_elements(self.display)
			pygame.display.update()
			
			# TICK
			self.clock.tick(FPS)
