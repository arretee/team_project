import pygame
import sys
from time import sleep

import screen
import game_field
import consts
import soldier
import database

state = {
    consts.STATE_RUNNING: True,
    consts.STATE_NIGHT_MODE: False,
}

save_keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_0]
pressed_keys = [False for key in save_keys]
timers_keys = [0 for key in save_keys]

def main():
    pygame.init()
    game_field.create_mines()
    game_field.create_bushes()
    soldier.create_player()
    
    # Create empty save data
    if not database.file_exists(consts.PATH_FILE_SAVE):
        database.create_empty_save(consts.PATH_FILE_SAVE)


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

        # Movemvent            
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
        
        # Night Mode activation
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                state[consts.STATE_NIGHT_MODE] = not state[consts.STATE_NIGHT_MODE]
                
                
        # Saves start timers 
        if event.type == pygame.KEYDOWN:
            for i, key in enumerate(save_keys):
                if event.key == key:
                    timers_keys[i] = pygame.time.get_ticks()
                    pressed_keys[i] = True
        
        # End timer and check time that button was pressed
        if event.type == pygame.KEYUP:
            for i, key in enumerate(save_keys):
                if event.key == key:
                    pressed_keys[i] = False
                    
                    pressed_time = pygame.time.get_ticks() - timers_keys[i]
                    
                    # Load data from memory
                    if pressed_time > consts.TIME_FOR_SAVE * 1000:
                        data = database.get_info_json(consts.PATH_FILE_SAVE, i)
                        if data is not None:
                            data_set(database.get_info_json(consts.PATH_FILE_SAVE, i))
                        
                    # Set data into memory
                    else:
                        database.save_data_into(i, consts.PATH_FILE_SAVE, True, soldier.player["body_positions"][0], state[consts.STATE_NIGHT_MODE], game_field.mines, game_field.bushes)
                        

def data_set(data: dict):
    """Function got dict from save file and updates data of the current game state

    Args:
        data (dict): data about game state
    """
    soldier.create_player(start_row = data[consts.DB_PLAYER_POS][0], start_col = data[consts.DB_PLAYER_POS][1])
    state[consts.STATE_NIGHT_MODE] = data[consts.DB_NIGHT_STATE]
    game_field.bushes = data[consts.DB_BUSHES]
    game_field.mines = data[consts.DB_MINES]
    
                
    
    

if __name__ == "__main__":
    main()