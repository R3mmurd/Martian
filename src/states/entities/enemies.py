"""
This file contains enemy states.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 7/24/20
"""
from src.states.entities.base_entity_state import BaseEntityState
from src.tilemap import TileMap
from src.game_object import GameObject

SNAIL_SPEED = 10


class SnailWalkState(BaseEntityState):
    def enter(self, inverted):
        self.entity.change_animation('walk')
        self.entity.inverted = inverted
        self.entity.vx = SNAIL_SPEED if self.entity.inverted else -SNAIL_SPEED

    def check_boundary(self):
        world_width = self.entity.game_level.tile_map.width
        if self.entity.x + self.entity.width > world_width:
            self.entity.x = world_width - self.entity.width
            return True
        elif self.entity.x < 0:
            self.entity.x = 0
            return True
        elif self.entity.vx > 0:
            # Snail row
            row = int(TileMap.to_i(self.entity.y))
            # Col of the right side of the snail
            col = int(TileMap.to_j(self.entity.x + self.entity.width))

            if not self.entity.check_solid_tile(row + 1, col, GameObject.TOP):
                return True
        elif self.entity.vx < 0:
            # Snail row
            row = int(TileMap.to_i(self.entity.y))
            # Col of the right side of the snail
            col = int(TileMap.to_j(self.entity.x))

            if not self.entity.check_solid_tile(row + 1, col, GameObject.TOP):
                return True

        return False

    def update(self, dt):
        self.entity.x += self.entity.vx*dt

        if self.check_boundary():
            self.entity.vx *= -1
            self.entity.inverted = not self.entity.inverted

