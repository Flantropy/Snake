import sys
import pygame
from random import randrange
from constants import *
from classes.snake import Snake
from classes.fruit import Fruit


class MainScene:
	def __init__(self):
		self.running = True
		pygame.init()
		self.display = pygame.display.set_mode(DISPLAY_SIZE)
		self.clock = pygame.time.Clock()
		self.snake = None
	
	def run(self):
		while self.running:
			#  HANDLE EVENTS
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					pygame.quit()
					sys.exit()
			# UPDATE AND RENDER
			pygame.display.update()
			
			# TICK
			self.clock.tick(FPS)
