"""
This file contains definitions enemy definitions.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 7/24/20
"""
from src.states.entities import enemies as enemy_states

import settings

ENEMIES = {
    'snail': {
        'yellow': {
            'width': settings.TILE_SIZE,
            'height': settings.TILE_SIZE,
            'texture': 'creatures',
            'animations': {
                'walk': {
                    'frames': [48, 49],
                    'interval': 0.25
                }
            },
            'states': {
                'walk': enemy_states.SnailWalkState
            },
            'first_state': 'walk'
        },
        'blue': {
            'width': settings.TILE_SIZE,
            'height': settings.TILE_SIZE,
            'texture': 'creatures',
            'animations': {
                'walk': {
                    'frames': [52, 53],
                    'interval': 0.25
                }
            },
            'states': {
                'walk': enemy_states.SnailWalkState
            },
            'first_state': 'walk'
        }
    }
}
