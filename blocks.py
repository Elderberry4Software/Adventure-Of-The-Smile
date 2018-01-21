import pygame
import random

#blocks

	#point block
pointBlocks = []

try:
	pointBlock_img = pygame.image.load("sprites/block/point_block.png") 
except:
	print("Cannot load point_block.png")

def spawn_point_block(x, y):
	pointBlock = {'surface': pointBlock_img,
			'size': 8,
			'x': x,
			'y': y}
	return pointBlock


	#health block
healthBlocks = []

try:
	healthBlock_img = pygame.image.load("sprites/block/health_block.png")
	healthBlock_rect = healthBlock_img.get_rect()
except:
	print("Cannot load healthBlock sprite")

def spawn_health_block(x, y):
	# get an (x, y). If there is a block there, change (x,y) again.
	healthBlock = {'surface': healthBlock_img,
			'size': 8,
			'x': x,
			'y': y}
	return healthBlock
