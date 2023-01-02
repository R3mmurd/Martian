"""
This file contains the class MartianGame that describes
a platformer.

Author: Alejandro Mujica (aledrums@gmail.com) 
Date: 07/19/2020
"""
from gale.game import Game
from gale.input_handler import InputHandler, InputListener
from gale.state_machine import StateMachine

import settings

from src.states import game


class MartianGame(Game, InputListener):
    def init(self):
        InputHandler.register_listener(self)
        self.state_machine = StateMachine({
            'start': game.StartState,
            'play': game.PlayState,
            'stats': game.StatsState,
        })
        self.state_machine.change('start')
        settings.GAME_SOUNDS['pickup_coin'].set_volume(0.25)

    def update(self, dt):
        self.state_machine.update(dt)

    def render(self, surface):
        self.state_machine.render(surface)

    def on_input(self, input_id, input_data):
        if input_id == 'quit' and input_data.pressed:
            self.quit()


if __name__ == '__main__':
    game = MartianGame(
        title='Super Martian', window_width=settings.WINDOW_WIDTH,
        window_height=settings.WINDOW_HEIGHT,
        virtual_width=settings.VIRTUAL_WIDTH,
        virtual_height=settings.VIRTUAL_HEIGHT
    )
    game.exec()
