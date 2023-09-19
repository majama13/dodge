import pygame
import random

class Obstacle(pygame.sprite.Sprite):

	
	def __init__(self, window):
	
		super().__init__()
		self.window = window
		self.image = pygame.Surface([0, 0])
		self.rect = pygame.Rect([0, 0, 0, 0])
		self.vel = 5
		self.accl = 0
		self.min_size = 40
		
	
	def spawn(self, delay = 0):

		#get random values for x, y, width, height
		self.rect.width = random.randint(self.min_size, self.window.get_width()//2)
		self.rect.height = random.randint(self.min_size, self.window.get_height()//2)
		self.rect.x = random.randint(0, self.window.get_width())
		if delay:
			self.rect.y = -self.rect.height * random.randint(1, delay)
		else:
			self.rect.y = -self.rect.height
		
		#update the surface to the above values
		self.image = pygame.Surface([self.rect.width, self.rect.height])
		self.image.fill((225, 225, 225))
		self.rect = self.image.get_rect(x = self.rect.x, y = self.rect.y)

		
	def update(self, time = 0):
				
		#update obstacle position
		if pygame.time.get_ticks() > time:
			if self.rect.y > self.window.get_height():
				self.spawn()
			self.rect.y += self.vel
			self.vel += self.accl	
	
	
	def reset(self):
		self.spawn(3)
