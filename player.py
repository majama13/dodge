import pygame

class Player(pygame.sprite.Sprite):

	
	def __init__(self, window, player_size):
	
		super().__init__()
		self.window = window
		self.bot = pygame.draw.circle(window, (120, 0, 0), (150, 150), 20)
		self.bot.center = window.get_rect().center
		self.radius = player_size
		self.vel = 5
		self.laser = pygame.Rect(self.bot.x, self.bot.y, 4, 24)
		self.lasershot = False
		
		
		
	def update(self, keys):
	
		#udate Player movement
		if self.bot.x > self.radius:
			self.bot.x -= keys[pygame.K_LEFT] * self.vel
		if self.bot.x < self.window.get_width() - self.radius:
			self.bot.x += keys[pygame.K_RIGHT] * self.vel
		if self.bot.y > self.radius:
			self.bot.y -= keys[pygame.K_UP] * self.vel
		if self.bot.y < self.window.get_height() - self.radius:
			self.bot.y += keys[pygame.K_DOWN] * self.vel
		
		#update laser movement
		if keys[pygame.K_SPACE] and not self.lasershot:
			self.lasershot = True
		elif self.laser.y < 0:
			self.lasershot = False
			self.laser.y = self.bot.y - 2 * self.radius
			self.laser.x = self.bot.x
		else:
			self.laser.y -= 2 * self.vel	
	
	
	
	def draw(self):
	
		#draw player
		pygame.draw.circle(self.window, (0, 225, 0), (self.bot.x, self.bot.y), self.radius, 3)
		
		#draw laser
		if self.lasershot:
			pygame.draw.rect(self.window, (225, 0, 0), self.laser)

		
