import consts
import random


# Create game objects
bushes = [] # Bush = {"row": x, "col": y}
mines = [] # Mine = [(row, col), (row1, col1), .... (rown, coln)] -> all positions that mine is on 

def create_bushes():
    """
        Function create bushes all over the screen
    """
    
    # Generate all possible positions
    positions = []
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            positions.append[(row, col)]


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
            
    # Set mines at random positions
    for i in range(consts.BUSHES_NUM):
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
                
                
create_mines()