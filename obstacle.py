import pygame

class Obstacle(pygame.sprite.Sprite):

	
	def __init__(self, window, x, y, width, height):
	
		super().__init__()
		self.window = window
		self.obst = pygame.Rect(x, y, width, height)
		self.vel = 5
		self.accl = 0
		
		
		
	def update(self):
		
		#update obstacle position
		self.obst.y += self.vel
		self.vel += self.accl	
	
	
	
	def draw(self):
		
		#draw obstacle
		pygame.draw.rect(self.window, (225, 225, 225), self.obst)
