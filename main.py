#! /usr/bin/env python3
import sys, os



#Pygame
import pygame
from pygame.locals import*


#my files
from lv import *
from music import *
from sound import *
from blocks import *
from enemies import *
from char import *





#inits
pygame.init()

clock = pygame.time.Clock()
fps = 60

window_size = width, hight = 320, 240

speed = 5
black = 0, 0, 0

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Adventure Of The Smile')

gameOverMode = False
#world settings


	#Colours
WHITE = (255, 255, 255)
BLUE = (0, 0, 128)
RED = (255, 0, 0) #NEVER USE BECAUSE DEFAULT LASER IS RED
GREEN = (0, 255, 0)
COLOURS = [WHITE,BLUE,GREEN]


random_colour = random.randint(0,2)
background_colour = COLOURS[random_colour]

def check_no_blocks():
	#checks if there are any point blocks
	if len(pointBlocks) == 0:
		#any health
		if len(healthBlocks) ==0:
			return True
		else:
			return False
		
	
def check_press():
	global moveLeft, moveRight
	for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			
			elif event.type == KEYDOWN:
				if event.key in (K_LEFT, K_a):
					moveRight = False
					moveLeft = True
				elif event.key in (K_RIGHT, K_d):
					moveLeft = False
					moveRight = True
				elif event.key in ( K_SPACE, K_UP):
					#fire laser
					lasers.append(shoot_laser(smile['x'] + 8, smile['y']))
			
			elif event.type == KEYUP:
				if event.key in (K_LEFT, K_a):
					moveLeft = False
				elif event.key in (K_RIGHT, K_d):
					moveRight = False
				elif event.key == K_ESCAPE:
					pass #pause()
	


def set_rects():
	
	if not gameOverMode:
			if moveLeft:
				smile['x'] -= SPEED
				if smile['x'] < 0:
					smile['x'] = 0
					
			if moveRight:
				smile['x'] += SPEED
				if smile['x'] > 288:
					smile['x'] = 288
	
	smile['rect'] = pygame.Rect( ( smile['x'],
								smile['y'], 
								smile['size'], 
								smile['size'] ) )
			
	for i in range(len(lasers)-1, -1, -1):
		las = lasers[i]
		#Check if laser "las" has hit something. If so, delete "las" and other object.
			# not sure yet.
		
		if las['y'] <= -16:
			del lasers[i]
		#Move lasers up
		las['y'] -= las['mv_y']
		
		las['rect'] = pygame.Rect( ( las['x'],
								las['y'],
								las['size'],
								las['size'] ) )
		
		
	#BLOCK RECTS
	for i in range(len(pointBlocks)-1, -1, -1):
		pntblok = pointBlocks[i]
		pntblok['rect'] = pygame.Rect( ( pntblok['x'],
									pntblok['y'],
									pntblok['size'],
									pntblok['size'] ) )
		
	for i in range(len(healthBlocks)-1, -1, -1):
		hlthblok = healthBlocks[i]
		hlthblok['rect'] = pygame.Rect( ( hlthblok['x'],
									hlthblok['y'],
									hlthblok['size'],
									hlthblok['size'] ) )
	for i in range(len(Squares)-1, -1, -1):
		sq = Squares[i]
		sq['rect'] = pygame.Rect( ( sq['x'],
								sq['y'],
								sq['size'],
								sq['size']
								) )


def update_points_text():
	points_font = pygame.font.SysFont("monospace", 15)
	points_amount = "{}".format(smile['points'])
	points_text = points_font.render( points_amount, 1, (255, 0, 0 ) )
	screen.blit(points_text, (0, 220) )


def update_health_text():
	health_font = pygame.font.SysFont("monospace", 15)
	health_amount = "{}".format(smile['health'])
	health_text = health_font.render( health_amount, 1, (255, 0, 0 ) )
	screen.blit(health_text, (300, 220) )


def update_screen():
	screen.fill(background_colour)
	
	
	try:
		#show pngs
		screen.blit(smile['surface'], smile['rect'])
	except:
		print("")
	
	
		#lasers
	try:
		for las in lasers:
			screen.blit(las['surface'], las['rect'])
	except:
		print("")
	
	
		#pointBlocks
	try:
		for pntblok in pointBlocks:
			screen.blit(pntblok['surface'], pntblok['rect'] )
	except:
		print("Cannot update \"Point block\" image")
	
		#healthBlocks
	try:
		for hlthblok in healthBlocks:
			screen.blit(hlthblok['surface'], hlthblok['rect'] )
	except:
		print("Cannot update \"Health block\" image")
	
	
	try:
		for sq in Squares:
			screen.blit(sq['surface'],sq['rect'])
	except:
		print("Cannot update \"Square enemy\" image")
	
	
	#update health text
	update_health_text()
	
	#update points text
	update_points_text()
	
	
	pygame.display.update()


def room_setup(room):
	random_colour = random.randint(0,2)
	background_colour = COLOURS[random_colour]
	
	i = 0
	while i < (10 * room):
		pointBlocks.append(spawn_point_block(random.randint(10, 300), random.randint(5, 180) ))
		i += 1
	i = 0
	while i < 5:
		healthBlocks.append(spawn_health_block(random.randint(10, 300), random.randint(5, 180) ))
		i +=1
	i = 0


def check_colisions_point_block():
	for i in range(len(lasers)-1, -1, -1):
		las = lasers[i]
		#point block
		for a in range(len(pointBlocks)-1, -1, -1):
			pntblok = pointBlocks[a]
			if 'rect' in las and pntblok['rect'].colliderect(las['rect']):
				smile['points'] += 100
				try:
					del lasers[i]
					del pointBlocks[a]
				except:
					print("lasers[i] out of range")


def check_colisions_health_block(): 
	for i in range(len(lasers)-1, -1, -1):
		las = lasers[i]
		#health block
		for h in range(len(healthBlocks)-1, -1, -1):
			hlthblok = healthBlocks[h]
			if 'rect' in las and hlthblok['rect'].colliderect(las['rect']):
				if smile['health'] < smile['max_health']:
					smile['health'] += 1
				try:
					del lasers[i]
					del healthBlocks[h]
				except:
					print("lasers[i] out of range")


def check_colisions():
	check_colisions_point_block()
	check_colisions_health_block()


def game():
	global moveLeft, moveRight, room
	
	
	room_setup(room)
	
	while True:
		check_press()
		set_rects()
		check_colisions()
		#spawn enemies
		spawn_Enemies(room)
			#move enemies
		move_enemies()
		bounce_Square_Enemies()
		delete_Enenies()
		
		if ( check_no_blocks() ):
			room += 1
			room_setup(room)
		
		
		#update screen
		update_screen()
		clock.tick(fps)


def main():
	
	
	try:
		pygame.mixer.music.play(-1, 0.0)
	except:
		print("Cannot play in-game music")
	
	game()

		
main()
