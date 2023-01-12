import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480 

x_ret = 300
y_ret = 240 
larg_ret = 10
alt_ret = 10


tela = pygame.display.set_mode((largura,altura))

vel_x = 0.1
vel_y = 0.5

while True:
	#tela.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
	
	if(vel_x > 0) and (x_ret + larg_ret >= largura):
		vel_x = vel_x*(-1) 
	if(vel_x < 0) and (x_ret <= 0):
		vel_x = vel_x*(-1) 

	if(vel_y > 0) and (y_ret + alt_ret >= altura):
		vel_y = vel_y*(-1)
	if(vel_y < 0) and (y_ret <= 0):
		vel_y = vel_y*(-1)

	x_ret = x_ret + vel_x
	y_ret = y_ret + vel_y

	pygame.draw.rect(tela, (0,255,0), (x_ret,y_ret,larg_ret,alt_ret))

	pygame.display.update()
