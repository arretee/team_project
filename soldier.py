import consts
import game_field

player =  {
    "body_positions":[], # List of lists with rows and colos: [[row1, col1], [row2, col2], [row3, col3], ....]
    "leg_positions":[]  # List of lists with rows and colos: [[row1, col1], [row2, col2]]]
}

def create_player(start_row: int = consts.PLAYER_START_ROW, start_col: int = consts.PLAYER_START_COL):
    for row in range(consts.PLAYER_ROWS):
        for col in range(consts.PLAYER_COLS):
            if row <= consts.PLAYER_ROWS - 2:
                player["body_positions"].append([start_row + row,start_col + col])
            else:
                player["leg_positions"].append([start_row + row,start_col + col])

def on_mine():
    for leg in player["leg_positions"]:
        for mine in game_field.mines:
            if tuple(leg) in mine:
                return True
    return False


def on_flag():

    flag_position = []
    for row in range(consts.FLAG_ROWS):
        for col in range(consts.FLAG_COLS):
            flag_position.append([consts.FLAG_ROW + row, consts.FLAG_COL + col])

    for body in player["body_positions"]:
        if body in flag_position:
            return True
    return False







def move(right: bool = False, left: bool = False, up: bool = False, down: bool = False):
    """Function is moving player in direction specified with args
        Can be specified more than one direction

    Args:
        right (bool, optional): move to right. Defaults to False.
        left (bool, optional): move to left. Defaults to False.
        up (bool, optional): move to up. Defaults to False.
        down (bool, optional): move down. Defaults to False.
    """
    
    direction = [0, 0]
    if right:
        direction[1] += 1
    if left:
        direction[1] -= 1
    if down:
        direction[0] += 1
    if up:
        direction[0] -= 1
    
    player_up, player_left = player["body_positions"][0]
    
    player_right = player_left + consts.PLAYER_COLS - 1
    player_down = player_up + consts.PLAYER_ROWS - 1
    
    can_be_moved = False
    
    # Check if new player pos is in range of board
    if 0 <= player_left + direction[1] <= consts.BOARD_COLS and 0 <= player_right + direction[1] < consts.BOARD_COLS:
        if 0 <= player_up + direction[0] <= consts.BOARD_ROWS and 0 <= player_down + direction[0] < consts.BOARD_ROWS:
            can_be_moved = True
            
            
    if can_be_moved:
        for i in range(len(player["body_positions"])):
            player["body_positions"][i][0] += direction[0]
            player["body_positions"][i][1] += direction[1]
        
        for i in range(len(player["leg_positions"])):
            player["leg_positions"][i][0] += direction[0]
            player["leg_positions"][i][1] += direction[1]
                    