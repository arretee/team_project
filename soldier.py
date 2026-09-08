import consts

player =  {
    "body_positions":[],
    "leg_positions":[]
}

def create_player():

    for row in range(consts.PLAYER_ROWS):
        for col in range(consts.PLAYER_COLS):
            if row <= consts.PLAYER_ROWS - 1:
                player["body_positions"].append((row,col))
            else:
                player["leg_positions"].append((row,col))
