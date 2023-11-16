import pygame
from game_parameters import *
pygame.init()

#SCREEN_WIDTH = 800
#SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Spritesheets")

# import sprite sheet
sprite_sheet_image = pygame.image.load('groundGrass_mown.png').convert()


# get images
def get_image(sheet, frame_x, frame_y, width, height):
    image = pygame.Surface((width, height)).convert()
    #image.set_colorkey((color))
    image.blit(sheet, (0, 0), (frame_x * width, frame_y * height, width, height))
    #image = pygame.transform.scale(image, (width * scale, height * scale))
    return image


# loop through sprite sheet to get images

frame = get_image(sprite_sheet_image, 0, 0, 64, 64)


run = False

while run:

    # update background
    screen.fill((0, 0, 0))

    # show frame image

    screen.blit(frame, (0, 0))

        # uncomment these if you want to see the figure moving on the screen
        # screen.fill(RGB)
        # screen.blit(all_frames[x], (75, 0))
        # pygame.display.flip()
        # clock.tick(30)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()