import pygame
import consts
import random


screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def fill_background():
    screen.fill(consts.COLOR_BACKGROUND)

    pygame.display.update()

