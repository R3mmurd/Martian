"""
This file contains a class that represents a game item.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/22/20
"""
from src.game_object import GameObject


class GameItem(GameObject):
    def __init__(self, collidable, consumable,
                 on_collide=None, on_consume=None,
                 *args, **kwargs):
        super(GameItem, self).__init__(*args, **kwargs)
        self.collidable = collidable
        self.consumable = consumable
        self._on_collide = on_collide
        self._on_consume = on_consume
        self.in_play = True

    def respawn(self, x=None, y=None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

        self.in_play = True

    def on_collide(self, another):
        if not self.collidable or self._on_collide is None:
            return None
        return self._on_collide(self, another)

    def on_consume(self, consumer):
        if not self.consumable:
            return None
        self.in_play = False
        return (None if self._on_consume is None
                else self._on_consume(self, consumer))
