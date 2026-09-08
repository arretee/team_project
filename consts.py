# Board
BOARD_ROWS = 25
BOARD_COLS = 50
CELL_SIZE = 20 # pixels per cell

# Window size
WINDOW_WIDTH = BOARD_COLS * CELL_SIZE
WINDOW_HEIGHT = BOARD_ROWS * CELL_SIZE

# Colors
COLOR_BACKGROUND = "#99ff99"
COLOR_BACKGROUND_NIGHT = "#003300"
COLOR_LINE = "#99ff99"

# Flag
FLAG_ROWS = 3
FLAG_COLS = 4

FLAG_ROW = BOARD_ROWS - FLAG_ROWS
FLAG_COL = BOARD_COLS - FLAG_COLS

# Mines
MINE_ROWS = 1
MINE_COLS = 3
MINES_NUM = 20


# Bushes
BUSHES_NUM = 20


# scale
SCALE_BUSH_ROW = 3
SCALE_BUSH_COLUMN = 3

SCALE_MINE_ROW = MINE_ROWS
SCALE_MINE_COLUMN = MINE_COLS

# States of program names
STATE_RUNNING = "running"
STATE_NIGHT_MODE = "night_mode"

# Player data
PLAYER_ROWS = 4
PLAYER_COLS = 2
PLAYER_START_ROW = 0
PLAYER_START_COL = 0
PLAYER_SCALE_ROW = 4
PLAYER_SCALE_COL =  4


# Paths
PATH_IMAGE_EXPLOTION = "images/explotion.png"
PATH_IMAGE_FLAG = "images/flag.png"
PATH_IMAGE_GRASS = "images/grass.png"
PATH_IMAGE_GUARD = "images/guard.png"
PATH_IMAGE_INJURY = "images/injury.png"
PATH_IMAGE_MINE = "images/mine.png"
PATH_IMAGE_SNAKE = "images/snake.png"
PATH_IMAGE_SOLDIER_NIGHT = "images/soldier_night.png"
PATH_IMAGE_SOLDIER = "images/soldier.png"
PATH_TELEPORT = "images/teleport.png"