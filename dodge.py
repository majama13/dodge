import pygame
import random
import player, obstacle


def generate_obstacle(window, player_size):
	
	width = random.randint(player_size * 2, window.get_width()//2)
	height = random.randint(player_size * 2, window.get_height()//2)
	x = random.randint(0, window.get_width())
	y = -height//2
	return obstacle.Obstacle(window, x, y, width, height)
	
	
def main():
	pygame.init()
	window = pygame.display.set_mode((300, 300))
	game_area = pygame.Rect(0, 0, 300, 300)
	clock = pygame.time.Clock()
	player_size = 20
	
	P1 = player.Player(window, player_size)
	O1 = generate_obstacle(window, player_size)
	FPS = 60

	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:
				print(pygame.key.name(event.key))
				
		keys = pygame.key.get_pressed()
		
		if O1.obst.y > window.get_height():
			O1.kill()
			O1 = generate_obstacle(window, player_size)
		
		P1.update(keys)
		O1.update()
		
		window.fill(0)
		P1.draw()
		O1.draw()
		pygame.display.flip()
		
	pygame.quit()
	exit()


if __name__ == '__main__':
	main()
