import pygame
import sys
from background import draw_background
from game_parameters import *

#initalizing the game
pygame.init()

#should create screen
screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Just a field')


#draw the initial background/make a copy of it
running=True
background=screen.copy()
draw_background(background)

while running:
    #lets the player leave when they want
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))
    pygame.display.flip()




while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()



pygame.quit()


#alright so I get a screen to pop up really fast and then my actual screen.
# It has to do with the sprite sheet but im not 100% sure why its doing it.