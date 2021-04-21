"""
This file contains the class MartianGame that describes
a platformer.

Author: Alejandro Mujica (aledrums@gmail.com) 
Date: 07/19/2020
"""
import pygame

from gale.game import Game
from gale.state_machine import StateMachine

import settings

from src.states import game


class MartianGame(Game):
    def init(self):
        self.state_machine = StateMachine({
            'start': game.StartState,
            'play': game.PlayState,
            'stats': game.StatsState,
        })
        self.state_machine.change('start')
        settings.GAME_SOUNDS['pickup_coin'].set_volume(0.25)

    def update(self, dt):
        self.state_machine.update(dt)
        settings.pressed_keys = {}

    def render(self, surface):
        self.state_machine.render(surface)

    def keydown(self, key):
        if key == pygame.K_ESCAPE:
            self.quit()
        settings.pressed_keys[key] = True


if __name__ == '__main__':
    game = MartianGame(
        title='Marty Martian', window_width=settings.WINDOW_WIDTH,
        window_height=settings.WINDOW_HEIGHT,
        virtual_width=settings.VIRTUAL_WIDTH,
        virtual_height=settings.VIRTUAL_HEIGHT
    )
    game.exec()
