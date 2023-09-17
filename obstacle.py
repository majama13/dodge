import pygame
import random

class Obstacle(pygame.sprite.Sprite):

	
	def __init__(self, window):
	
		super().__init__()
		self.window = window
		self.obst = pygame.Rect(0, 0, 0, 0)
		self.vel = 5
		self.accl = 0
		self.min_size = 40
		
	
	def spawn(self):

		self.obst.width = random.randint(self.min_size, self.window.get_width()//2)
		self.obst.height = random.randint(self.min_size, self.window.get_height()//2)
		self.obst.x = random.randint(0, self.window.get_width())
		self.obst.y = -self.obst.height

		
	def update(self, time = 0):
				
		#update obstacle position
		if pygame.time.get_ticks() > time:
			if self.obst.y > self.window.get_height():
				self.spawn()
			self.obst.y += self.vel
			self.vel += self.accl	
	
	
	def draw(self):
		
		#draw obstacle
		pygame.draw.rect(self.window, (225, 225, 225), self.obst)
