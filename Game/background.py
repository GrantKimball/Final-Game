import pygame
from game_parameters import *

#draw background and sprites
def draw_background(field, image):

    # fill screen
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            field.blit(image, (x, y))
