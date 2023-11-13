import pygame
from game_parameters import *


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))






def draw_background(field):
    # fill screen
    for x in range(0, SCREEN_HEIGHT, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            field.blit(water, (x, y))
