"""
This file contains the implementation of a game level

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/23/20
"""
from src.tilemap import Tile, TileMap
from src.game_item import GameItem
from src.enemy import Enemy
from src.defs import tiles, items, enemies

import settings


class GameLevel:
    def __init__(self, level=1):
        self.level = level
        self.tile_map = None
        self.items = []
        self.enemies = []
        self._load_map()

    def _load_map(self):
        with open(f'maps/world-{self.level}.txt', 'r') as f:
            r, c = f.readline().split(' ')
            r, c = int(r), int(c)
            self.tile_map = TileMap(r, c)

            for i in range(r):
                col = f.readline()
                if col[-1] == '\n':
                    col = col[:-1]
                col = col.split(' ')

                for j in range(c):
                    tile_def = tiles.TILES[col[j]]
                    x, y = TileMap.to_screen(i, j)
                    self.tile_map.tiles[i][j] = Tile(
                        x, y, tile_def['solidness'], tile_def['frame']
                    )

            num_items = int(f.readline())

            for _ in range(num_items):
                coin_line = f.readline()
                if coin_line[-1] == '\n':
                    coin_line = coin_line[:-1]
                item, i, j = coin_line.split(' ')
                i, j = int(i), int(j)

                name, color = item.split('-')
                item_def = items.ITEMS[name]
                x, y = TileMap.to_screen(i, j)
                self.items.append(
                    GameItem(
                        x=x, y=y, width=settings.TILE_SIZE,
                        height=settings.TILE_SIZE, texture=item_def['texture'],
                        frame=item_def['frame'][color],
                        consumable=item_def['consumable'],
                        collidable=item_def['collidable'],
                        on_consume=item_def['on_consume'][color],
                        solidness=item_def['solidness']
                    )
                )

            num_enemies = int(f.readline())

            for _ in range(num_enemies):
                enemy_line = f.readline()
                if enemy_line[-1] == '\n':
                    enemy_line = enemy_line[:-1]
                enemy, i, j, direction = enemy_line.split(' ')
                i, j = int(i), int(j)

                name, color = enemy.split('-')
                enemy_def = enemies.ENEMIES[name][color]

                x, y = TileMap.to_screen(i, j)
                inverted = direction == 'r'

                self.enemies.append(Enemy(x, y, inverted, self, **enemy_def))

    def render(self, surface):
        self.tile_map.render(surface)

        for item in self.items:
            if not item.in_play:
                continue
            item.render(surface)

        for enemy in self.enemies:
            enemy.render(surface)
