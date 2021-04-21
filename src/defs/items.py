"""
This file contains definitions item definitions.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/24/20
"""
import random

import settings

from gale.timer import Timer


def pickup_coin(player, coin, points, color, time):
    settings.GAME_SOUNDS['pickup_coin'].play()
    player.score += points
    player.coin_counter[color] += 1
    Timer.after(time, lambda: coin.respawn())


def pickup_green_coin(coin, player):
    pickup_coin(player, coin, 1, 'green', random.uniform(2, 4))


def pickup_blue_coin(coin, player):
    player.coin_counter['blue'] += 1
    pickup_coin(player, coin, 5, 'blue', random.uniform(5, 8))


def pickup_red_coin(coin, player):
    pickup_coin(player, coin, 20, 'red', random.uniform(5, 15))


def pickup_yellow_coin(coin, player):
    pickup_coin(player, coin, 50, 'yellow', random.uniform(17, 21))


ITEMS = {
    'coin': {
        'texture': 'tiles',
        'solidness': dict(top=False, right=False, bottom=False, left=False),
        'consumable': True,
        'collidable': True,
        'on_consume': {
            'yellow': pickup_yellow_coin,
            'blue': pickup_blue_coin,
            'red': pickup_red_coin,
            'green': pickup_green_coin
        },
        'frame': {
            'yellow': 54,
            'blue': 61,
            'red': 55,
            'green': 62
        }
    }
}
