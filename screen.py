import pygame
import consts
import random

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def fill_background():
    screen.fill(consts.COLOR_BACKGROUND)

def draw_bushes(bush_list):

    size_pic = (consts.CELL_SIZE * consts.SCALE_BUSH_COLUMN, consts.CELL_SIZE * consts.SCALE_BUSH_ROW)
    bush_pic = pygame.image.load(consts.PATH_IMAGE_GRASS)
    bush_pic = pygame.transform.scale(bush_pic, size_pic)

    pygame.Surface.set_colorkey(bush_pic, consts.COLOR_BACKGROUND)

    for bush in bush_list:

        bush_rect = bush_pic.get_rect(topleft=(bush["row"] * consts.CELL_SIZE,bush["col"] * consts.CELL_SIZE))
        screen.blit(bush_pic, bush_rect)


def draw_mines(mine_list):
    mine_pic = pygame.image.load(consts.PATH_IMAGE_MINE)
    size_pic = (consts.CELL_SIZE * consts.SCALE_MINE_COLUMN, consts.CELL_SIZE * consts.SCALE_MINE_ROW)
    mine_pic = pygame.transform.scale(mine_pic, size_pic)

    for mine in mine_list:

        mine_rect = mine_pic.get_rect(topleft=(mine[0][1] * consts.CELL_SIZE, mine[0][0] * consts.CELL_SIZE))
        screen.blit(mine_pic, mine_rect)



def draw(state):
    fill_background()

    draw_bushes([
        {"row": 20, "col": 4},
        {"row": 33,  "col": 15},
        {"row": 1, "col": 10}
    ])

    draw_mines([
        [(3, 2), (3, 3), (3, 4)],
        [(7, 5), (7, 6), (7, 7)],
        [(20, 24), (20, 24), (20, 24)],
        [(24, 9), (24, 10), (24, 11)]
    ])

    pygame.display.update()