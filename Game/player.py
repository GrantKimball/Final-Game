import pygame
from game_parameters import *
#create pygame class for a player

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        #make the fish flip when going left
        self.forward_image=pygame.image.load('../assets/sprites/orange_fish.png')
        self.reverse_image=pygame.transform.flip(self.forward_image, True, False)
        self.image=self.forward_image
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.rect.center=(x,y)
        self.x_speed=0
        self.y_speed=0