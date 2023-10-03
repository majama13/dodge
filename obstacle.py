import pygame
import random

class Obstacle(pygame.sprite.Sprite):

	
	def __init__(self, window, player_size, parent = None):
	
		super().__init__()
		self.window = window
		self.image = pygame.Surface([0, 0])
		self.rect = pygame.Rect([0, 0, 0, 0])
		self.vel = 5.00
		self.min_size = player_size * 2
		self.color = (225, 225, 225)
		self.parent = parent
		
	
	def spawn(self):

		#get random values for x, y, width, height
		self.rect.width = random.randint(self.min_size, self.window.get_width()//2)
		self.rect.height = random.randint(self.min_size, self.window.get_height()//2)
		self.rect.x = random.randint(0, self.window.get_width())
		if self.parent and self.parent.rect.y < 0:
			self.rect.y = self.parent.rect.y - (self.rect.height + 2 * self.min_size)
		else:
			self.rect.y = -self.rect.height

		
		#update the surface to the above values
		self.image = pygame.Surface([self.rect.width, self.rect.height])
		self.image.fill(self.color)
		self.rect = self.image.get_rect(x = self.rect.x, y = self.rect.y)

		
	def update(self, restart = False):
				
		#if restart == True:
		#	self.vel = 5.00

		#update obstacle position
		if self.rect.y > self.window.get_height():
			self.vel += 0.1
			self.spawn()
		self.rect.y += self.vel
	
	
	def reset(self):
		self.vel = 5.00
		self.spawn()


