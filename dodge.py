import pygame
import player, obstacle, laser

class Dodge():

	def __init__(self):

		pygame.init()

		self.WIDTH, self.HEIGHT = 300, 600
		self.BLACK = (0, 0, 0)
		self.WHITE = (225, 225, 225)

		self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		self.game_area = pygame.Rect(0, 0, self.WIDTH, self.HEIGHT)
		self.clock = pygame.time.Clock()
		self.player_size = 20
		self.FPS = 60	
		self.keys = None
		self.run = True
		self.game_over = False
		
		#create sprites
		self.player_sprites = pygame.sprite.Group()
		self.P1 = player.Player(self.window, self.player_size)
		self.player_sprites.add(self.P1)

		self.laser_sprites = pygame.sprite.Group()
		self.laser = laser.Laser(self.P1.radius)
		self.laser_sprites.add(self.laser)
		
		self.obst_sprites = pygame.sprite.Group()
		self.O1 = obstacle.Obstacle(self.window)
		self.O2 = obstacle.Obstacle(self.window)
		self.O3 = obstacle.Obstacle(self.window)
		self.obst_sprites.add(self.O1)
		self.obst_sprites.add(self.O2)
		self.obst_sprites.add(self.O3)

	
	def reset_game(self):

		self.P1.reset()
		for sprite in self.obst_sprites:
			sprite.reset()

	def endgame(self):
		#reset the game
		self.window.fill(self.WHITE)

		FONT1 = pygame.font.Font(None, 36)
		FONT2 = pygame.font.Font(None, 24)
		endgame_message1 = FONT1.render("Game Over", True, self.BLACK)
		endgame_message2 = FONT2.render("Press any key to continue playing", True, self.BLACK)
		message_rect1 = endgame_message1.get_rect(center = (self.WIDTH // 2, self.HEIGHT // 2 - 25))
		message_rect2 = endgame_message2.get_rect(center = (self.WIDTH // 2, self.HEIGHT // 2 + 25))
		self.window.blit(endgame_message1, message_rect1)
		self.window.blit(endgame_message2, message_rect2)

		pygame.display.flip()

		self.reset_game()

		waiting = True
		while waiting:
			self.clock.tick(self.FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				if event.type == pygame.KEYDOWN:					
					waiting = False


	def main(self):
 
		self.run = True
		while self.run:
			self.clock.tick(self.FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.run = False
				if event.type == pygame.KEYDOWN:					
					print(pygame.key.name(event.key))

			self.keys = pygame.key.get_pressed()
			
			#update sprites
			self.O1.update()
			self.O2.update(900)	# add a time delay before spawning the next obstacles
			self.O3.update(900*2)
			self.player_sprites.update(self.keys)
			self.laser_sprites.update(self.keys, self.P1.rect.center[0], self.P1.rect.center[1])

			#draw sprites
			self.window.fill(0)

			self.obst_sprites.draw(self.window)
			self.player_sprites.draw(self.window)
			if self.laser.lasershot:
				self.laser_sprites.draw(self.window)

			pygame.display.flip()

			#check collision
			if pygame.sprite.groupcollide(self.player_sprites, self.obst_sprites, False, False):				
				self.game_over = True
				self.endgame()

		pygame.quit()
		exit()


if __name__ == '__main__':
	Dodge().main()
