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

def add_football(num_football):
    for _ in range(num_football):
        footballs.add(Football(random.randint(50, SCREEN_WIDTH-50),50))