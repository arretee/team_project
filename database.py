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


def create_empty_save(path: str):
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
        
    with open(path, "w") as f:
        json.dump(empty_data, f)



def get_info_json(path: str, saved_num):
    with open(path, "r") as file:
        data = json.load(file)

    if not data[str(saved_num)][consts.DB_IS_SAVED]:
        return
    return data[str(saved_num)]




def save_data_into(save_num: int, path: str, is_saved:bool, player_pos:list, night_state: bool, mines: list, bushes:list):
    """
        Function saves data into an save file in relevant save number

    Args:
        save_num (int): number of sate to save the data into
        path (str): path of save file
        is_saved (bool): if data is relevant
        player_pos (list): player top left position
        night_state (bool): night mode is active
        mines (list): mines list
        bushes (list): bushes list
    """

    with open(path) as f:
        data = json.load(f)

    data[str(save_num)] = {
            consts.DB_IS_SAVED: is_saved,
            consts.DB_PLAYER_POS: player_pos,
            consts.DB_NIGHT_STATE: night_state,
            consts.DB_MINES: mines,
            consts.DB_BUSHES: bushes
        }

    with open(path, "w") as f:
        json.dump(data, f)

