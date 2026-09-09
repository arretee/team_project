import consts

direction = []
guard = []



def create_guard(row:int = consts.GUARD_START_ROW, col: int = consts.GUARD_START_COL):
    """
        Create guard start vaiables
    """
    global direction
    global guard
    
    direction = consts.GUARD_START_DIRECTION.copy()
    guard = []
    
    for i in range(consts.GUARD_ROWS):
        for j in range(consts.GUARD_COLS):
            guard.append([row + i, col + j])
            
            
def move_guard():
    """
        Function to move guard in direction of guard
    """
    
    for pos in guard:
        pos[0] += direction [0]
        pos[1] += direction [1]


def update_direction():
    """
        Function check direction of an guard and updates it if it reached the wall
    """
    
    guard_left = guard[0][1]
    guard_right = guard[-1][1]
    
    
    if guard_left == 0:
        direction[1] = -direction[1]
        
    if guard_right + 1 == consts.BOARD_COLS:
        direction[1] = -direction[1]
        