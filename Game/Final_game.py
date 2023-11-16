import pygame
import sys
from background import draw_background
from game_parameters import *
from player import Player

#initalizing the game
pygame.init()

#initialize clock
clock=pygame.time.Clock()

#should create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Just a field with a guy')

# import sprite sheet
sprite_sheet_image = pygame.image.load('groundGrass_mown.png').convert()
#creates a 64x64 surface to put stuff on
image = pygame.Surface((64, 64)).convert()
#puts an image onto the surface above
image.blit(sprite_sheet_image, (0, 0), (0, 0, 64, 64))

#creating a player at a certain spot
player = Player(SCREEN_WIDTH/1.2,SCREEN_HEIGHT/1.2)

#draw the initial background/make a copy of it
running = True
background = screen.copy()
draw_background(background, image)



while running:
    #lets the player leave when they want
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('pressed key left')
                player.move_left()
            if event.key == pygame.K_RIGHT:
                print('pressed key right')
                player.move_right()
    #continuously blits screen
    screen.blit(background, (0,0))
    #updates player
    player.update()
    player.draw(screen)
    #continuously shows the updated screen
    pygame.display.flip()

    clock.tick(60)



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

#pygame.quit()


