"""
This file contains functions to generate quads to get elements
from an "atlas" (a texture with multiple sprites).

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/14/2020
"""
import pygame


def generate_quads(atlas, tile_width, tile_height):
    """
    Given and atlas, this function builds a list of quads based on
    atlas dimensions, tile width, and tile height.

    :param atlas: surace with the texture.
    :param tile_width: with of the sprite.
    :param tile_height: Height of the sprite.
    """
    atlas_width, atlas_height = atlas.get_size()

    num_cols = atlas_width//tile_width
    num_rows = atlas_height//tile_height

    spritesheet = []

    for i in range(num_rows):
        for j in range(num_cols):
            spritesheet.append(
                pygame.Rect(
                    j * tile_width,   # x position
                    i * tile_height,  # y position
                    tile_width, tile_height
                )
            )

    return spritesheet
