import pygame
from typing import Tuple, List

# Display configuration
SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
FRAME_RATE: int = 60
WINDOW_TITLE: str = "Ali's Birthday Celebration"

# Color definitions (R, G, B)
COLOR_BACKGROUND: Tuple[int, int, int] = (10, 10, 25)
COLOR_TEXT_MAIN: Tuple[int, int, int] = (255, 105, 180)  # Hot Pink
COLOR_TEXT_SHADOW: Tuple[int, int, int] = (255, 20, 147)  # Deep Pink
COLOR_HEART: Tuple[int, int, int] = (220, 20, 60)        # Crimson

# Text styling
TEXT_CONTENT: str = "Ali"
FONT_SIZE: int = 150
# 3D depth effect offset in pixels
TEXT_DEPTH_OFFSET: int = 5

# Heart animation parameters
HEART_COUNT: int = 30
HEART_SIZE_MIN: int = 10
HEART_SIZE_MAX: int = 30
HEART_SPEED_Y_MIN: float = 0.5
HEART_SPEED_Y_MAX: float = 2.0
HEART_SPEED_X_MAX: float = 1.0
HEART_ALPHA_MIN: int = 50
HEART_ALPHA_MAX: int = 200

# Initialization
pygame.font.init()

# Font settings (will attempt to load default system serif/sans-serif if not found)
try:
    TITLE_FONT: pygame.font.Font = pygame.font.SysFont("arialblack", FONT_SIZE)
except (pygame.error, RuntimeError):
    TITLE_FONT: pygame.font.Font = pygame.font.SysFont(None, FONT_SIZE) # type: ignore