import pygame

from src.quad_util import generate_quads

# Size of each tile
TILE_SIZE = 16

# Tile map dimensions
MAP_ROWS = 12
MAP_COLS = 50

# Size we're trying to emulate
VIRTUAL_WIDTH = 25*TILE_SIZE
VIRTUAL_HEIGHT = MAP_ROWS*TILE_SIZE

# Size of our actual window
WINDOW_WIDTH = VIRTUAL_WIDTH*4
WINDOW_HEIGHT = VIRTUAL_HEIGHT*4

# A value for gravity
GRAVITY = 980

# Martian dimensions
PLAYER_WIDTH = 16
PLAYER_HEIGHT = 20

BACKGROUND_TILE = -3

# Sound effects
GAME_SOUNDS = {
    'pickup_coin': pygame.mixer.Sound('sounds/pickup_coin.wav'),
    'jump': pygame.mixer.Sound('sounds/jump.wav'),
    'timer': pygame.mixer.Sound('sounds/timer.wav'),
    'count': pygame.mixer.Sound('sounds/count.wav'),
}

# Graphics
GAME_TEXTURES = {
    'martian': pygame.image.load('graphics/martian.png'),
    'tiles':  pygame.image.load('graphics/tileset.png'),
    'creatures':  pygame.image.load('graphics/creatures.png'),
}

# Quad frames
GAME_FRAMES = {
    'martian': generate_quads(GAME_TEXTURES['martian'], 16, 20),
    'tiles': generate_quads(GAME_TEXTURES['tiles'], 16, 16),
    'creatures': generate_quads(GAME_TEXTURES['creatures'], 16, 16),
}

# Fonts
GAME_FONTS = {
    'tiny': pygame.font.Font('fonts/font.ttf', 6),
    'small': pygame.font.Font('fonts/font.ttf', 8),
    'medium': pygame.font.Font('fonts/font.ttf', 16),
    'large': pygame.font.Font('fonts/font.ttf', 20),
}

# Dictionary of pressed keys
pressed_keys = {}

# Variable to indicate that game is paused
paused = False
