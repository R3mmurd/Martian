"""
This file contains the implementation of the class Enemy

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 7/24/20
"""
from src.entity import Entity


class Enemy(Entity):
    def __init__(self, x, y, inverted, game_level, **defs):
        super(Enemy, self).__init__(
            x, y, defs['width'], defs['height'], defs['texture'],
            game_level,
            states={
                state_name: lambda sm: state_class(self, sm)
                for state_name, state_class in defs['states'].items()
            },
            animations=defs['animations']
        )
        self.change_state(defs['first_state'], inverted)
