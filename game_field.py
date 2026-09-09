import consts
import random

import soldier

# Create game objects
bushes = [] # Bush = {"row": x, "col": y}
mines = [] # Mine = [(row, col), (row1, col1), .... (rown, coln)] -> all positions that mine is on
teleports = []

def create_bushes():
    """
        Function create bushes all over the screen
    """
    
    # Generate all possible positions
    positions = []
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            positions.append((row, col))


    # Set bushes on random positions
    for bush in range(consts.BUSHES_NUM):
        pos = random.choice(positions)
        
        positions.remove(pos)   # Remove position from the list 
        
        bushes.append(
                {
                    "row": pos[0],
                    "col": pos[1]
                }
            )
        
        
def create_mines():
    """
        Function creates mines all over the screen randomly
    """
    
    # Generate all possible positions
    positions = []
    for row in range(consts.BOARD_ROWS - consts.MINE_ROWS + 1):
        for col in range(consts.BOARD_COLS - consts.MINE_COLS + 1):
            positions.append((row, col))
            
            
    # Remove player start pos 
    for row in range(consts.PLAYER_ROWS):
        for col in range(consts.PLAYER_COLS):
            if (row, col) in positions:
                positions.remove((row, col)) 
            
            
    # Set mines at random positions
    for i in range(consts.MINES_NUM):
        pos = random.choice(positions)
        
        # create mine
        mine = []
        for row in range(consts.MINE_ROWS):
            for col in range(consts.MINE_COLS):
                mine.append((pos[0] + row, pos[1] + col))
        
        mines.append(mine)
        
        # create temp mine 
        temp_mine = []
        for row in range(consts.MINE_ROWS):
            for col in range(consts.MINE_COLS):
                temp_mine.append((pos[0] + row - consts.MINE_ROWS + 1, pos[1] + col - consts.MINE_COLS + 1))
                
                
        # Remove postions of create mize and temp mine from positions
        for pos in temp_mine + mine:
            if pos in positions:
                positions.remove(pos)

def create_teleports():

    positions = []

    for row in range(consts.BOARD_ROWS - consts.TELEPORT_ROWS + 1):
        if consts.START_ROW_TELEPORT <= row <= consts.STOP_ROW_TELEPORT:
            for col in range(consts.BOARD_COLS - consts.TELEPORT_COLS + 1):
                positions.append((row, col))

    for row in range(consts.PLAYER_ROWS):
        for col in range(consts.PLAYER_COLS):
            if (row, col) in positions:
                positions.remove((row, col))

    for i in range(consts.TELEPORTS_NUM):
        pos = random.choice(positions)

        teleport = []
        for row in range(consts.TELEPORT_ROWS):
            for col in range(consts.TELEPORT_COLS):
                teleport.append((pos[0] + row, pos[1] + col))

        teleports.append(teleport)

def pick_teleport(teleports_list):
    picked_teleport = random.choice(teleports_list)
    soldier.create_player(picked_teleport[0] - 5, picked_teleport[0])
