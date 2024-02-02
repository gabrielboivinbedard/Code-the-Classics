from enum import Enum
# Set up constants

class Control(Enum):
    PLAYER1 = 1
    PLAYER2 = 2
    AI = 3

WIDTH = 800
HEIGHT = 480
TITLE = "Boing!"

HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

PLAYER_SPEED = 6
MAX_AI_SPEED = 6