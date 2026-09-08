# Board
BOARD_ROWS = 25
BOARD_COLS = 50
CELL_SIZE = 20 # pixels per cell

# Window size
WINDOW_WIDTH = BOARD_COLS * CELL_SIZE
WINDOW_HEIGHT = BOARD_ROWS * CELL_SIZE

# Colors
COLOR_BACKGROUND = "#00b33c"
COLOR_BACKGROUND_NIGHT = "#003300"
COLOR_LINE = "#00b33c"

# Sizes
FLAG_ROWS = 3
FLAG_COLS = 4

MINE_ROWS = 1
MINE_COLS = 3

# Number Of objects
BUSHES_NUM = 20
MINES_NUM = 20



# Cells in game field matrix 
EMPTY_CELL = 0
MINE_CELL = 1
FLAG_CELL = 2

# States of program names
STATE_RUNNING = "running"
STATE_NIGHT_MODE = "night_mode"




# Positions
FLAG_ROW = BOARD_ROWS - FLAG_ROWS
FLAG_COL = BOARD_COLS - FLAG_COLS


# Paths
PATH_IMAGE_EXPLOTION = "images/explotion.png"
PATH_IMAGE_FLAG = "images/flag.png"
PATH_IMAGE_GRASS = "images/grass.png"
PATH_IMAGE_GUARD = "images/guard.png"
PATH_IMAGE_INJURY = "image/injury.png"
PATH_IMAGE_MICE = "image/mine.png"
PATH_IMAGE_SNAKE = "image/snake.png"
PATH_IMAGE_SOLDIER_NIGHT = "image/soldier_night.png"
PATH_IMAGE_SOLDIER = "image/soldier.png"
PATH_TELEPORT = "images/teleport.png"