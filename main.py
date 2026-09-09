import pygame
import sys
from time import sleep

import screen
import game_field
import consts
import soldier

state = {
    consts.STATE_RUNNING: True,
    consts.STATE_NIGHT_MODE: False,
}


def main():
    pygame.init()
    game_field.create_mines()
    game_field.create_bushes()
    soldier.create_player()


    # Main game loop
    while state[consts.STATE_RUNNING]:
        event_hanlder()
        
        screen.draw(state)
        

        if soldier.on_mine():
            state[consts.STATE_RUNNING] = False
            screen.draw_message(consts.LOSE_MESSAGE, consts.MESSAGE_POS, consts.MESSAGE_SIZE, consts.LOSE_MESSAGE_COLOR)
            sleep(5)
            
            
        elif soldier.on_flag():
            state[consts.STATE_RUNNING] = False
            screen.draw_message(consts.WIN_MESSAGE, consts.MESSAGE_POS, consts.MESSAGE_SIZE, consts.WIN_MESSAGE_COLOR)
            sleep(5)
            
            
            
            
    pygame.quit()
    sys.exit()

def event_hanlder():
    """
        Function for event handale from user input.
        Implemented with pygame events
        
    """
    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT:
            state["running"] = False
            
        if not state[consts.STATE_NIGHT_MODE]:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    soldier.move(right=True)
                if event.key == pygame.K_LEFT:
                    soldier.move(left=True)
                if event.key == pygame.K_UP:
                    soldier.move(up=True)
                if event.key == pygame.K_DOWN:
                    soldier.move(down=True)
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                state[consts.STATE_NIGHT_MODE] = not state[consts.STATE_NIGHT_MODE]
    
    

if __name__ == "__main__":
    main()