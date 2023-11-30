import pygame
from game_parameters import *
class Player2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        #makes the player flip when going left/right
        self.forward_image=pygame.image.load('characterRed (3).png')
        self.reverse_image=pygame.transform.flip(self.forward_image, True, False)
        self.image=self.forward_image
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.rect.center=(x,y)
        self.x_speed=0
        self.y_speed=0

    def move_left2(self):
        self.x_speed=-1*PLAYER_SPEED
        self.image=self.reverse_image

    def move_right2(self):
        self.x_speed=PLAYER_SPEED
        self.image=self.forward_image

    def stop2(self):
        self.x_speed=0
        self.y_speed=0

    def update2(self):
        #make sure player doesn't go offscreen (these are adjusted because the player is so small)
        if self.x>(SCREEN_WIDTH-TILE_SIZE)+30:
            self.x=(SCREEN_WIDTH-TILE_SIZE)+30
        if self.x<5:
            self.x=5
        #not really needed unless I decide to add an up and down button
        if self.y>SCREEN_HEIGHT-TILE_SIZE:
            self.y=SCREEN_HEIGHT-TILE_SIZE
        if self.y<0:
            self.y=0
        self.x+=self.x_speed
        self.y+=self.y_speed
        self.rect.x=self.x
        self.rect.y=self.y

    def draw2(self, field):
        field.blit(self.image, self.rect)