import pygame





	#Player
MAX_HEALTH = 9
INVULN = False
INVULN_TIME = 12
moveLeft = False
moveRight = False
SPEED = 4
smile_speed = 5


try:
	smile_img = pygame.image.load ("sprites/smile/smile_main.png")
	smile_img.convert_alph()
	smile_rect = smile_img.get_rect()
except:
	print("Cannot load \"smile_main.png\" AKA main smile ")

smile = {'surface': smile_img,
	'size': 32,
	'x': 160,
	'y': (240-32),
	'health': MAX_HEALTH,
	'max_health': MAX_HEALTH,
	'points': 0 }


lasers = []
try:
	laser_img = pygame.image.load("sprites/lasers/default_red_laser.png")
	laser_img.convert_alpha()
	laser_rect = laser_img.get_rect() 
except:
	print("Cannot load \"default_red_laser.png\"")

def shoot_laser(x, y):
	laser = {'surface': laser_img,
		'size':16,
		'x': x,
		'y': y,
		'mv_x': 0,
		'mv_y': 5}
	return laser


