#Enemies
import pygame
import random




	#Scribble


	#Squares
Squares = []

try:
	enemy_square_img = pygame.image.load("sprites/enemy/enemy_square_img.png")
	enemy_square_img.convert_alpha()
	enemy_square_rect = enemy_square_img.get_rect() 
except:
	print("Cannot load \"default_red_laser.png\"")

def spawn_Square(x, y):
	ra = random.randint(0,1)
	random_direction = 'left'
	if ra == 0:
		random_direction = 'left'
	else: #Obviously == 1
		random_direction = 'right'
	
	
	square = {'surface': enemy_square_img,
		'size':8,
		'x': x,
		'y': y,
		'mv_x': 2,
		'mv_y': 2,
		'direction': random_direction}
	return square

	#Rectangle


def move_enemies():
	for i in range( len(Squares)-1, -1, -1):
		sq = Squares[i]
		sq['y'] += sq['mv_y']
		if sq['direction'] == 'left':
			sq['x'] -= sq['mv_x']
		elif sq['direction'] == 'right':
			sq['x'] += sq['mv_x']





	###################Spawn Enemies
def spawn_Enemies(room):
	i = 1
	#spawn Squares
	amount = room
	if room >= 150:
		amount = 150
	r = random.randint(1, int(150/room ) )
	if r == 1:
		Squares.append( spawn_Square( random.randint(64, 305) , 0) )

def bounce_Square_Enemies():
	for i in range(len(Squares)-1, -1, -1):
		sq = Squares[i]
		if sq['x'] <= 0:
			sq['direction'] = 'right'
		elif sq['x'] >=(320-8):
			sq['direction'] = 'left'

def delete_Enenies():
		#Squares
	for i in range(len(Squares)-1, -1, -1):
		sq = Squares[i]
		if sq['y'] >= 240:
			del Squares[i]

