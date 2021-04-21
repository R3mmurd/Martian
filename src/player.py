"""
This file contains the implementation of the class Player.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/21/20
"""
from src.states.entities import player as player_states
from src.entity import Entity

import settings


class Player(Entity):
    def __init__(self, x, y, game_level):
        super(Player, self).__init__(
            x, y, settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT, 'martian',
            game_level,
            states={
                'idle': lambda sm: player_states.IdleState(self, sm),
                'walk': lambda sm: player_states.WalkState(self, sm),
                'jump': lambda sm: player_states.JumpState(self, sm),
                'fall': lambda sm: player_states.FallState(self, sm),
            },
            animations={
                'idle': {
                    'frames': [0]
                },
                'walk': {
                    'frames': [9, 10],
                    'interval': 0.15
                },
                'jump': {
                    'frames': [2]
                }
            }
        )
        self.score = 0
        self.coin_counter = {
            'yellow': 0,
            'red': 0,
            'blue': 0,
            'green': 0
        }
        self.dead = False
