import pygame
import player, obstacle

class Dodge():

	def __init__(self):
		self.window = pygame.display.set_mode((300, 600))
		self.game_area = pygame.Rect(0, 0, 300, 600)
		self.clock = pygame.time.Clock()
		self.player_size = 20
		self.FPS = 60	
		
		self.P1 = player.Player(self.window, self.player_size)
		self.O1 = obstacle.Obstacle(self.window)
		self.O2 = obstacle.Obstacle(self.window)
		self.O3 = obstacle.Obstacle(self.window)
		
		
	def main(self):
		pygame.init()
		
		run = True
		while run:
			self.clock.tick(self.FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
				if event.type == pygame.KEYDOWN:
					print(pygame.key.name(event.key))
					
			keys = pygame.key.get_pressed()
		
			self.P1.update(keys)
			self.O1.update()
			self.O2.update(900)	# add a time delay before spawning the next obstacles
			self.O3.update(900*2)
			
			self.window.fill(0)
			self.P1.draw()
			self.O1.draw()
			self.O2.draw()
			self.O3.draw()
			pygame.display.flip()
			
		pygame.quit()
		exit()


if __name__ == '__main__':
	Dodge().main()
