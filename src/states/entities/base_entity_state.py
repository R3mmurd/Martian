"""
This file contains the implementation of a base entity state.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 7/24/20
"""
from gale.state_machine import BaseState


class BaseEntityState(BaseState):
    def __init__(self, entity, state_machine):
        super(BaseEntityState, self).__init__(state_machine)
        self.entity = entity
