import pygame
from classes.snake import Snake


class EventHandler:
	def __init__(self):
		pass
	
	def handle_events(self, snake: Snake):
		for event in pygame.event.get():
			self.check_quit_event(event)
			self.check_keyboard_event(event, snake)
	
	@staticmethod
	def check_quit_event(event):
		if event.type == pygame.QUIT or \
				(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			pygame.quit()
			quit()
	
	@staticmethod
	def check_keyboard_event(event, snake: Snake):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				snake.turn("left")
			elif event.key == pygame.K_DOWN:
				snake.turn("down")
			elif event.key == pygame.K_RIGHT:
				snake.turn("right")
			elif event.key == pygame.K_UP:
				snake.turn("up")
