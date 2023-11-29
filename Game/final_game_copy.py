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
pygame.display.set_caption('Field, guy, balls, music')

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

#init score
score=0
score_font= pygame.font.Font("DragonHunter-9Ynxj.otf", 33)

#set number of lives
lives=3
lives_font= pygame.font.Font("DragonHunter-9Ynxj.otf", 33)

#restart font
restart_font=pygame.font.Font("DragonHunter-9Ynxj.otf", 75)

#draw the initial background/make a copy of it
running = True
background = screen.copy()
draw_background(background, image)

#load sound effects
catch_sound=pygame.mixer.Sound("Oh Yeah sound Effect.mp3")
game_music=pygame.mixer.Sound("2019-12-11_-_Retro_Platforming_-_David_Fesliyan.mp3")
hard_music=pygame.mixer.Sound("2021-08-30_-_Boss_Time_-_www.FesliyanStudios.com.mp3")
no_catch=pygame.mixer.Sound("Loud WHAAAAAAAAAAAAAAT sound effect.mp3")
end_music=pygame.mixer.Sound("Shutoku Mukai - Dandy in Love.mp3")

#play theme song
pygame.mixer.Sound.play(game_music)


#andre helping hand when I do the welcome screen
game=True
while game:
    while running and lives > 0:
        # lets the player leave when they want
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            player.stop()
            # allows you to move left and right
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print('pressed key left')
                    player.move_left()
                if event.key == pygame.K_RIGHT:
                    print('pressed key right')
                    player.move_right()
        # continuously blits screen
        screen.blit(background, (0, 0))
        # updates player
        player.update()
        # updates the footballs position and visibility
        footballs.update()

        # check to see if the player touches football
        result = pygame.sprite.spritecollide(player, footballs, True)
        if result:
            pygame.mixer.Sound.play(catch_sound)
            score += len(result)
            add_football(len(result))

        # check to see if the balls are off the screen
        for ball in footballs:
            if ball.rect.y >= SCREEN_HEIGHT:
                footballs.remove(ball)  # remove football from sprite group
                pygame.mixer.Sound.play(no_catch)
                lives = lives - 1
                add_football(1)

        # draw player
        player.draw(screen)

        # draw the sprites on the screen(flip ACTUALLY does it but this will tell them where to go)
        footballs.draw(screen)

        # draw/update the score
        text = score_font.render(f'Score : {score}', True, (255, 0, 0))
        screen.blit(text, (SCREEN_WIDTH - 178, 32))

        # lives
        lives_text = lives_font.render(f'Lives : {lives}', True, (255, 0, 0))
        screen.blit(lives_text, (23, 32))

        # continuously shows the updated screen
        pygame.display.flip()

        clock.tick(60)

    # after you lose

    # want to play only this music once you lose
    pygame.mixer.Sound.stop(game_music)
    pygame.mixer.Sound.play(end_music)

    # display restart option
    restart_text = restart_font.render(f'RESTART', True, (255, 0, 0))
    screen.blit(restart_text, ((SCREEN_WIDTH / 2) - 160, SCREEN_HEIGHT / 2))
    clickable_rect = pygame.Rect(200, 150, 600, 350)
    pygame.display.flip()
    new_game = True
    while new_game:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(mouse_x, mouse_y)
                if clickable_rect.collidepoint(mouse_x, mouse_y):
                    new_game = False




    # screen.blit(background, (0,0))
    pygame.display.flip()
    lives = 3
    score = 0
    add_football(5)
    continue

    #while True:
    #    for event in pygame.event.get():
    #        if event.type == pygame.QUIT:
    #            pygame.quit()
    #            sys.exit()

#add a restart option (mouse down function)

#pygame.quit()    this would make the game exit out

