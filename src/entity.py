"""
This file contains the implementation of the class Entity.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/20/2020
"""
from gale.state_machine import StateMachine

from src.mixins import DrawableMixin, AnimatedMixin, CollisionMixin
from src.tilemap import TileMap
from src.game_object import GameObject


class Entity(DrawableMixin, AnimatedMixin, CollisionMixin):
    def __init__(self, x, y, width, height, texture, game_level,
                 states={}, animations={}):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vx = 0
        self.vy = 0
        self.texture = texture
        self.game_level = game_level
        self.tile_map = self.game_level.tile_map
        self.state_machine = StateMachine(states)
        self.inverted = False
        self.animations = {}
        self._generate_animations(animations)

    def change_state(self, state, *args, **kwargs):
        self.state_machine.change(state, *args, **kwargs)

    def update(self, dt):
        self.state_machine.update(dt)
        AnimatedMixin.update(self, dt)

    def check_tile_collision(self, i, j, boundary):
        tile = self.tile_map.get_tile(i, j)
        return (tile is not None and tile.solidness[boundary]
                and self.collides(tile))

    def check_bottom_collision(self):
        cr = self.get_collision_rect()

        # Row for the center of the player
        i = TileMap.to_i(cr.centery)
        # Left and right columns
        left = TileMap.to_j(cr.left)
        right = TileMap.to_j(cr.right)

        if (self.check_tile_collision(i + 1, left, GameObject.TOP)
                or self.check_tile_collision(i + 1, right, GameObject.TOP)):
            self.y = TileMap.to_y(i + 1) - self.height
            return True

        return False

    def check_top_collision(self):
        cr = self.get_collision_rect()

        # Row for the center of the player
        i = TileMap.to_i(cr.centery)
        # Left and right columns
        left = TileMap.to_j(cr.left)
        right = TileMap.to_j(cr.right)

        if (self.check_tile_collision(i - 1, left, GameObject.BOTTOM)
                or self.check_tile_collision(i - 1, right, GameObject.BOTTOM)):
            self.y = TileMap.to_y(i)
            return True

        return False

    def check_left_collision(self):
        cr = self.get_collision_rect()

        # Column for the center of the player
        j = TileMap.to_j(cr.centerx)
        # Top and bottom Rows
        top = TileMap.to_i(cr.top)
        bottom = TileMap.to_i(cr.bottom)

        if (self.check_tile_collision(top, j - 1, GameObject.RIGHT)
                or self.check_tile_collision(bottom, j - 1, GameObject.RIGHT)):
            self.x = TileMap.to_x(j)
            return True

        return False

    def check_right_collision(self):
        cr = self.get_collision_rect()

        # Column for the center of the player
        j = TileMap.to_j(cr.centerx)
        # Top and bottom Rows
        top = TileMap.to_i(cr.top)
        bottom = TileMap.to_i(cr.bottom)

        if (self.check_tile_collision(top, j + 1, GameObject.LEFT)
                or self.check_tile_collision(bottom, j + 1, GameObject.LEFT)):
            self.x = TileMap.to_x(j + 1) - self.width
            return True

        return False

    def check_solid_tile(self, i, j, boundary):
        tile = self.tile_map.get_tile(i, j)
        return tile is not None and tile.solidness[boundary]

    def check_solid_under(self):
        cr = self.get_collision_rect()

        # Row for the center of the player
        i = TileMap.to_i(cr.centery)
        # Left and right columns
        left = TileMap.to_j(cr.left)
        right = TileMap.to_j(cr.right)
        return (self.check_solid_tile(i + 1, left, GameObject.TOP)
                or self.check_solid_tile(i + 1, right, GameObject.TOP))
