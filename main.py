import pygame
import sys
import screen

import consts

state = {
    consts.STATE_RUNNING: True,
    consts.STATE_NIGHT_MODE: False,
}

def main():
    pygame.init()
    
    
    # Main game loop
    while state["running"]:
        event_hanlder()
    
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
    
    

if __name__ == "__main__":
    main()