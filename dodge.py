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
		self.score = 0
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


	def show_endgame_screen(self):

		self.window.fill(self.WHITE)
		
		score_font = pygame.font.Font(None, 72)
		game_over_font = pygame.font.Font(None, 36)
		restart_font = pygame.font.Font(None, 24)
		
		score_message = score_font.render(str(self.score), True, self.BLACK)
		game_over_message = game_over_font.render("Game Over", True, self.BLACK)
		restart_message = restart_font.render("Press any key to continue playing", True, self.BLACK)
		score_rect = score_message.get_rect(center = (self.WIDTH // 2, self.HEIGHT // 2 - 100))
		game_over_rect = game_over_message.get_rect(center = (self.WIDTH // 2, self.HEIGHT // 2 + 0))
		restart_rect = restart_message.get_rect(center = (self.WIDTH // 2, self.HEIGHT // 2 + 50))
		self.window.blit(score_message, score_rect)
		self.window.blit(game_over_message, game_over_rect)
		self.window.blit(restart_message, restart_rect)

		pygame.display.flip()

		self.reset_game()

		waiting = True
		while waiting:
			self.clock.tick(self.FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()
				if event.type == pygame.KEYDOWN:					
					waiting = False
					self.score = pygame.time.get_ticks()


	def main(self):
 
		self.run = True
		while self.run:
			self.clock.tick(self.FPS)
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.run = False
				#if event.type == pygame.KEYDOWN:					
					#print(pygame.key.name(event.key))

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
				self.score = (pygame.time.get_ticks() - self.score)//100
				self.game_over = True
				self.show_endgame_screen()

		pygame.quit()
		exit()


if __name__ == '__main__':
	Dodge().main()
