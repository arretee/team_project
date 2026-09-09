import os
import consts

import json


def file_exists(path: str):
    """Check if file exists in some path

    Args:
        path (str): file path to check

    Returns:
        if file exists: True, false otherwise       
    """     
    
    if os.path.isfile(path):
        return True
    
    return False


def create_json(path: str):
    """Function to create saves file with no data inside.

    Args:
        path (str): path to file
    """
    empty_data = {}
    
    for i in range(consts.SAVES_NUMBERS):
        empty_data[i] = {
            consts.DB_IS_SAVED: False,
            consts.DB_PLAYER_POS: (),
            consts.DB_NIGHT_STATE: False,
            consts.DB_MINES: [],
            consts.DB_BUSHES: []
        }
        
    with open("sample.json", "w") as f:
        json.dump(empty_data, f)



def get_info_json(path: str, saved_num):
    with open(path, "r") as file:
        data = json.load(file)

    if not data[str(saved_num)][consts.DB_IS_SAVED]:
        return
    return data[str(saved_num)]

