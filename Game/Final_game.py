import pygame
import sys
from background import draw_background, add_football
from game_parameters import *
from player import Player
from football import *

#initalizing the game
pygame.init()

#initialize clock object
clock=pygame.time.Clock()

#should create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Field, guy, ball')

# import sprite sheet
sprite_sheet_image = pygame.image.load('groundGrass_mown.png').convert()
#creates a 64x64 surface to put stuff on
image = pygame.Surface((64, 64)).convert()
#puts an image onto the surface above
image.blit(sprite_sheet_image, (0, 0), (0, 0, 64, 64))

#draw footballs
add_football(5)

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
    #updates the footballs position and visibility
    footballs.update()

    #check to see if the player touches football
    result = pygame.sprite.spritecollide(player, footballs, True)
    if result:
    #    pygame.mixer.Sound.play(chomp)
    #    score += len(result)
        add_football(len(result))

    #check to see if the balls are off the screen
    for ball in footballs:
        if ball.y >= ball.rect.height: #aight this is messin something up
            footballs.remove(ball)#remove football from sprite group
            add_football(1)

    #draw player
    player.draw(screen)

    #draw the sprites on the screen(flip ACTUALLY does it but this will tell them where to go)
    footballs.draw(screen)

    #continuously shows the updated screen
    pygame.display.flip()


    clock.tick(60)


#screen.blit(background, (0,0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

#pygame.quit()


