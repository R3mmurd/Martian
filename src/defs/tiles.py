"""
This file contains definitions tile definitions.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/23/20
"""
# Solidness definitions
TOP_SOLID = dict(top=True, right=False, bottom=False, left=False)
FULL_SOLID = dict(top=True, right=True, bottom=True, left=True)
NO_SOLID = dict(top=False, right=False, bottom=False, left=False)

TILES = {
    # TOP GROUNDS
    'TLG': {
        'frame': 0,
        'solidness': TOP_SOLID,
    },
    'TG': {
        'frame': 1,
        'solidness': TOP_SOLID,
    },
    'TRG': {
        'frame': 2,
        'solidness': TOP_SOLID,
    },
    'ATLG': {
        'frame': 3,
        'solidness': TOP_SOLID,
    },
    'ATG': {
        'frame': 4,
        'solidness': TOP_SOLID,
    },
    'ATRG': {
        'frame': 5,
        'solidness': TOP_SOLID,
    },
    # GROUNDS
    'LG': {
        'frame': 7,
        'solidness': NO_SOLID,
    },
    'G': {
        'frame': 8,
        'solidness': NO_SOLID,
    },
    'RG': {
        'frame': 9,
        'solidness': NO_SOLID,
    },
    # BOTTOM GROUNDS
    'BLG': {
        'frame': 14,
        'solidness': NO_SOLID,
    },
    'BG': {
        'frame': 15,
        'solidness': NO_SOLID,
    },
    'BRG': {
        'frame': 16,
        'solidness': NO_SOLID,
    },
    'B': {
        'frame': 41,
        'solidness': FULL_SOLID,
    },
    # EMPTY
    'E': {
        'frame': -1,
        'solidness': NO_SOLID,
    },
    # WATER
    'W': {
        'frame': 40,
        'solidness': NO_SOLID,
    },
    # PLANTS
    'BUSH': {
        'frame': 48,
        'solidness': NO_SOLID,
    },
    'CACTUS': {
        'frame': 45,
        'solidness': NO_SOLID,
    },
    # TREE
    'TT': {
        'frame': 23,
        'solidness': NO_SOLID,
    },
    'TM': {
        'frame': 30,
        'solidness': NO_SOLID,
    },
    'TB': {
        'frame': 37,
        'solidness': NO_SOLID,
    },
    # CLOUD
    'CT': {
        'frame': 53,
        'solidness': NO_SOLID,
    },
    'CM': {
        'frame': 60,
        'solidness': NO_SOLID,
    },
    'CB': {
        'frame': 67,
        'solidness': NO_SOLID,
    },
}
