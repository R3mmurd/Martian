"""
This file contains the implementation of the player states.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/21/20
"""
import pygame

from gale.input_handler import InputHandler, InputListener

from src.states.entities.base_entity_state import BaseEntityState

import settings

PLAYER_SPEED = 80


class IdleState(BaseEntityState, InputListener):
    def enter(self):
        InputHandler.register_listener(self)
        self.entity.vx = 0
        self.entity.change_animation('idle')

    def exit(self):
        InputHandler.unregister_listener(self)

    def on_input(self, input_id, input_data):
        if input_id == 'jump' and input_data.pressed:
            self.entity.change_state('jump')

        keys = pygame.key.get_pressed()

        if input_id == 'left' and input_data.pressed:
            self.entity.change_state('walk', 'left')
        elif input_id == 'right' and input_data.pressed:
            self.entity.change_state('walk', 'right')


class WalkState(BaseEntityState, InputListener):
    def enter(self, direction):
        InputHandler.register_listener(self)
        self.entity.inverted = direction == 'left'
        self.entity.vx = PLAYER_SPEED
        if self.entity.inverted:
            self.entity.vx *= -1
        self.entity.change_animation('walk')

    def exit(self):
        InputHandler.unregister_listener(self)

    def on_input(self, input_id, input_data):
        if input_id == 'jump' and input_data.pressed:
            self.entity.change_state('jump')

        if input_id == 'left':
            if input_data.pressed:
                self.entity.inverted = True
                self.entity.vx = -PLAYER_SPEED
            elif input_data.released and self.entity.vx <= 0:
                self.entity.change_state('idle')
        elif input_id == 'right':
            if input_data.pressed:
                self.entity.inverted = False
                self.entity.vx = PLAYER_SPEED
            elif input_data.released and self.entity.vx >= 0:
                self.entity.change_state('idle')

    def update(self, dt):
        if not self.entity.check_solid_under():
            self.entity.change_state('fall')

        next_x = self.entity.x + self.entity.vx * dt
        if self.entity.vx < 0:
            self.entity.x = max(0, next_x)
        else:
            self.entity.x = min(
                self.entity.tile_map.width - self.entity.width, next_x
            )

        if (self.entity.check_left_collision()
                or self.entity.check_right_collision()):
            self.entity.vx = 0


class JumpState(BaseEntityState, InputListener):
    def enter(self):
        InputHandler.register_listener(self)
        settings.GAME_SOUNDS['jump'].play()
        self.entity.change_animation('jump')
        self.entity.vy = -settings.GRAVITY/3

    def exit(self):
        InputHandler.unregister_listener(self)

    def on_input(self, input_id, input_data):
        if input_id == 'left':
            if input_data.pressed:
                self.entity.inverted = True
                self.entity.vx = -PLAYER_SPEED
            elif input_data.released and self.entity.vx <= 0:
                self.entity.vx = 0
        elif input_id == 'right':
            if input_data.pressed:
                self.entity.inverted = False
                self.entity.vx = PLAYER_SPEED
            elif input_data.released and self.entity.vx >= 0:
                self.entity.vx = 0

    def update(self, dt):
        self.entity.vy += settings.GRAVITY * dt

        if self.entity.check_top_collision():
            self.entity.vy = 0

        if self.entity.vy >= 0:
            self.entity.change_state('fall')

        next_x = self.entity.x + self.entity.vx * dt
        if self.entity.vx < 0:
            self.entity.x = max(0, next_x)
        else:
            self.entity.x = min(
                self.entity.tile_map.width - self.entity.width, next_x
            )
        if (self.entity.check_left_collision()
                or self.entity.check_right_collision()):
            self.entity.vx = 0

        self.entity.y += self.entity.vy * dt


class FallState(BaseEntityState, InputListener):
    def enter(self):
        InputHandler.register_listener(self)
        self.entity.change_animation('jump')

    def exit(self):
        InputHandler.unregister_listener(self)

    def on_input(self, input_id, input_data):
        if input_id == 'left':
            if input_data.pressed:
                self.entity.inverted = True
                self.entity.vx = -PLAYER_SPEED
            elif input_data.released and self.entity.vx <= 0:
                self.entity.vx = 0
        elif input_id == 'right':
            if input_data.pressed:
                self.entity.inverted = False
                self.entity.vx = PLAYER_SPEED
            elif input_data.released and self.entity.vx >= 0:
                self.entity.vx = 0

    def update(self, dt):
        next_x = self.entity.x + self.entity.vx * dt
        if self.entity.vx < 0:
            self.entity.x = max(0, next_x)
        else:
            self.entity.x = min(
                self.entity.tile_map.width - self.entity.width, next_x
            )

        if (self.entity.check_left_collision()
                or self.entity.check_right_collision()):
            self.entity.vx = 0

        self.entity.vy += settings.GRAVITY*dt
        self.entity.y += self.entity.vy*dt

        if self.entity.check_bottom_collision():
            if self.entity.vx > 0:
                self.entity.change_state('walk', 'right')
            elif self.entity.vx < 0:
                self.entity.change_state('walk', 'left')
            else:
                self.entity.change_state('idle')
