import pygame
import consts
import game_field
import soldier
import guard

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def fill_background(color):
    screen.fill(color)

def draw_bushes(bush_list):

    size_pic = (consts.CELL_SIZE * consts.SCALE_BUSH_COLUMN, consts.CELL_SIZE * consts.SCALE_BUSH_ROW)
    bush_pic = pygame.image.load(consts.PATH_IMAGE_GRASS)
    bush_pic = pygame.transform.scale(bush_pic, size_pic)

    pygame.Surface.set_colorkey(bush_pic, consts.COLOR_BACKGROUND)

    for bush in bush_list:

        bush_rect = bush_pic.get_rect(topleft=(bush["col"] * consts.CELL_SIZE,bush["row"] * consts.CELL_SIZE))
        screen.blit(bush_pic, bush_rect)


def draw_mines(mine_list):
    mine_pic = pygame.image.load(consts.PATH_IMAGE_MINE)
    size_pic = (consts.CELL_SIZE * consts.SCALE_MINE_COLUMN, consts.CELL_SIZE * consts.SCALE_MINE_ROW)
    mine_pic = pygame.transform.scale(mine_pic, size_pic)

    for mine in mine_list:

        mine_rect = mine_pic.get_rect(topleft=(mine[0][1] * consts.CELL_SIZE, mine[0][0] * consts.CELL_SIZE))
        screen.blit(mine_pic, mine_rect)


def draw_flag():
    flag_pic = pygame.image.load(consts.PATH_IMAGE_FLAG)
    size_pic = (consts.CELL_SIZE * consts.FLAG_COLS, consts.CELL_SIZE * consts.FLAG_ROWS)
    flag_pic = pygame.transform.scale(flag_pic, size_pic)

    flag_rect = flag_pic.get_rect(topleft=(consts.FLAG_COL* consts.CELL_SIZE , consts.FLAG_ROW * consts.CELL_SIZE))
    screen.blit(flag_pic, flag_rect)


def draw_soldier(pic_path):
    soldier_pic = pygame.image.load(pic_path)
    size_pic = (consts.CELL_SIZE * consts.PLAYER_SCALE_COL, consts.CELL_SIZE * consts.PLAYER_SCALE_ROW)
    soldier_pic = pygame.transform.scale(soldier_pic, size_pic)

    soldier_rect = soldier_pic.get_rect(topleft=((soldier.player["body_positions"][0][1]-1) * consts.CELL_SIZE, soldier.player["body_positions"][0][0] * consts.CELL_SIZE))
    screen.blit(soldier_pic, soldier_rect)


def draw_grid():
    for x in range(0, consts.WINDOW_WIDTH, consts.CELL_SIZE):
        for y in range(0, consts.WINDOW_HEIGHT, consts.CELL_SIZE):
            rect = pygame.Rect(x, y, consts.CELL_SIZE, consts.CELL_SIZE)
            pygame.draw.rect(screen, consts.COLOR_LINE, rect, 1)
            
            
def draw_guard():
    """
        Function draws guard on the screen
    """
    guard_pic = pygame.image.load(consts.PATH_IMAGE_GUARD)
    guard_pic = pygame.transform.scale(guard_pic, (consts.CELL_SIZE * consts.GUARD_COLS, consts.CELL_SIZE * consts.GUARD_ROWS))
    
    if guard.direction[1] < 0:
        guard_pic = pygame.transform.flip(guard_pic, True, False)
        
    guard_rect = guard_pic.get_rect(topleft=(guard.guard[0][1] * consts.CELL_SIZE, guard.guard[0][0] * consts.CELL_SIZE))
        
    screen.blit(guard_pic, guard_rect)
    


def draw_day_mode():
    fill_background(consts.COLOR_BACKGROUND)
    draw_bushes(game_field.bushes)
    draw_guard()
    draw_flag()
    draw_soldier(consts.PATH_IMAGE_SOLDIER)

def draw_night_mode():
    fill_background(consts.COLOR_BACKGROUND_NIGHT)
    draw_grid()
    draw_guard()
    draw_mines(game_field.mines)
    draw_soldier(consts.PATH_IMAGE_SOLDIER_NIGHT)


def draw_message(text:str, pos:list, size:int, color: str):
    """Draw message on the screen

    Args:
        text (str): text to display
        pos (list): positon of center
        size (int): size of text
        color (str): color string
    """
    
    font = pygame.font.SysFont("Arial", size)
    image = font.render(text, False, color)
    rect = image.get_rect(center = pos)
    
    screen.blit(image, rect)
    pygame.display.update()


def draw(state):

    if state[consts.STATE_NIGHT_MODE]:
        draw_night_mode()
    else:
        draw_day_mode()

    pygame.display.update()