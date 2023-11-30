import pygame
import random
from game_parameters import *
#creates a class for the football, which we can call in other files
class Football(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image=pygame.image.load('ball_football.png').convert()
        self.image.set_colorkey((0,0,0))
        self.image=pygame.transform.scale(self.image, (30,30))
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.speed=random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center=(x,y)

#Continuously updates the position (it says where itll go and then the draw function actually puts in there)
    def update(self):
        self.y +=self.speed
        self.rect.y=self.y
    def draw(self, field):
        field.blit(self.image,self.rect)

#creates a football group
footballs=pygame.sprite.Group()
def remove_footballs():
    # Kill all sprites in the group
    footballs.empty()

