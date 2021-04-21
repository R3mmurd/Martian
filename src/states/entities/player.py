"""
This file contains the implementation of the player states.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/21/20
"""
import pygame

from src.states.entities.base_entity_state import BaseEntityState

import settings

PLAYER_SPEED = 80


class IdleState(BaseEntityState):
    def enter(self):
        self.entity.vx = 0
        self.entity.change_animation('idle')

    def update(self, dt):
        if settings.pressed_keys.get(pygame.K_SPACE):
            self.entity.change_state('jump')

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.entity.change_state('walk', 'left')
        elif keys[pygame.K_RIGHT]:
            self.entity.change_state('walk', 'right')


class WalkState(BaseEntityState):
    def enter(self, direction):
        self.entity.inverted = direction == 'left'
        self.entity.change_animation('walk')

    def update(self, dt):
        if settings.pressed_keys.get(pygame.K_SPACE):
            self.entity.change_state('jump')

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.entity.inverted = True
            self.entity.vx = -PLAYER_SPEED
        elif keys[pygame.K_RIGHT]:
            self.entity.inverted = False
            self.entity.vx = PLAYER_SPEED
        else:
            self.entity.change_state('idle')

        if not self.entity.check_solid_under():
            self.entity.change_state('fall')

        next_x = self.entity.x + self.entity.vx*dt
        if self.entity.vx < 0:
            self.entity.x = max(0, next_x)
        else:
            self.entity.x = min(
                self.entity.tile_map.width - self.entity.width, next_x
            )

        if (self.entity.check_left_collision()
                or self.entity.check_right_collision()):
            self.entity.vx = 0


class JumpState(BaseEntityState):
    def enter(self):
        settings.GAME_SOUNDS['jump'].play()
        self.entity.change_animation('jump')
        self.entity.vy = -settings.GRAVITY/3

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.entity.inverted = True
            self.entity.vx = -PLAYER_SPEED
        elif keys[pygame.K_RIGHT]:
            self.entity.inverted = False
            self.entity.vx = PLAYER_SPEED
        else:
            self.entity.vx = 0

        self.entity.vy += settings.GRAVITY*dt

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

        self.entity.y += self.entity.vy*dt


class FallState(BaseEntityState):
    def enter(self):
        self.entity.change_animation('jump')

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.entity.inverted = True
            self.entity.vx = -PLAYER_SPEED
        elif keys[pygame.K_RIGHT]:
            self.entity.inverted = False
            self.entity.vx = PLAYER_SPEED
        else:
            self.entity.vx = 0

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
