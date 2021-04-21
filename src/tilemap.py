"""
This file contains the implementation of Tile and TileMap.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/21/20
"""
from src.mixins import CollisionMixin
from src.game_object import GameObject

import settings


class Tile(GameObject, CollisionMixin):
    def __init__(self, x, y, solidness, frame):
        super(Tile, self).__init__(
            texture='tiles', frame=frame, solidness=solidness,
            x=x, y=y, width=settings.TILE_SIZE, height=settings.TILE_SIZE
        )


class TileMap:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.tiles = [[None for _ in range(cols)] for _ in range(rows)]

        self.width = cols*settings.TILE_SIZE
        self.height = rows*settings.TILE_SIZE

    def get_tile(self, i, j):
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols:
            return None
        return self.tiles[i][j]

    @staticmethod
    def to_map(x, y):
        """
        Get the row and column (i, j) components in the map for
        the position (x, y).
        """
        return TileMap.to_i(y), TileMap.to_j(x)

    @staticmethod
    def to_i(y):
        return y//settings.TILE_SIZE

    @staticmethod
    def to_j(x):
        return x//settings.TILE_SIZE

    @staticmethod
    def to_screen(i, j):
        """
        Get the the screen position (x, y) for the row i and column j.
        """
        return TileMap.to_x(j), TileMap.to_y(i)

    @staticmethod
    def to_y(i):
        return i*settings.TILE_SIZE

    @staticmethod
    def to_x(j):
        return j*settings.TILE_SIZE

    def render(self, surface):
        for tile_row in self.tiles:
            for tile in tile_row:
                surface.blit(
                    settings.GAME_TEXTURES['tiles'], (tile.x, tile.y),
                    settings.GAME_FRAMES['tiles'][settings.BACKGROUND_TILE]
                )
                tile.render(surface)
