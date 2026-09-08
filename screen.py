import pygame
import consts
import random

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def fill_background():
    screen.fill(consts.COLOR_BACKGROUND)

def draw_bushes(bush_list):

    bush_pic = pygame.image.load(consts.PATH_IMAGE_GRASS).convert()

    for bush in bush_list:



        bush_rect = bush_pic.get_rect()
        screen.blit(bush_pic, bush_rect)


def draw(state):
    fill_background()

    draw_bushes([
        {"row": 1,
         "col": 1}
    ])

    pygame.display.update()