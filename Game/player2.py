import pygame
from game_parameters import *
class Player2(pygame.sprite.Sprite):
    def __init__(self,x2,y2):
        super().__init__()
        #makes the player flip when going left/right
        self.forward_image2=pygame.image.load('characterRed (3).png')
        self.reverse_image2=pygame.transform.flip(self.forward_image2, True, False)
        self.image2=self.forward_image2
        self.rect=self.image2.get_rect()
        self.x2=x2
        self.y2=y2
        self.rect.center=(x2,y2)
        self.x_speed2=0
        self.y_speed2=0

    def move_left2(self):
        self.x_speed2=-1*PLAYER_SPEED
        self.image2=self.reverse_image2

    def move_right2(self):
        self.x_speed2=PLAYER_SPEED
        self.image2=self.forward_image2

    def stop2(self):
        self.x_speed2=0
        self.y_speed2=0

    def update2(self):
        #make sure player doesn't go offscreen (these are adjusted because the player is so small)
        if self.x2>(SCREEN_WIDTH-TILE_SIZE)+30:
            self.x2=(SCREEN_WIDTH-TILE_SIZE)+30
        if self.x2<5:
            self.x2=5
        #not really needed unless I decide to add an up and down button
        if self.y2>SCREEN_HEIGHT-TILE_SIZE:
            self.y2=SCREEN_HEIGHT-TILE_SIZE
        if self.y2<0:
            self.y2=0
        self.x2+=self.x_speed2
        self.y2+=self.y_speed2
        self.rect.x=self.x2
        self.rect.y=self.y2

    def draw2(self, field):
        field.blit(self.image2, self.rect)