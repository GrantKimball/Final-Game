import pygame
from game_parameters import *
from football import Football, footballs
import random

#draw background and sprites
def draw_background(field, image):

    # fill screen
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            field.blit(image, (x, y))
#this is messing stuff up. It is just supposed to draw the title on the top of the screen
    custom_font = pygame.font.Font("ball_football.png", 50)
    text = custom_font.render('CATCH EM ALL', True, (255, 0, 0))
    field.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, SCREEN_HEIGHT - 550 - text.get_height() / 2))

def add_football(num_football):
    for _ in range(num_football):
        footballs.add(Football(random.randint(50, SCREEN_WIDTH-50),15))