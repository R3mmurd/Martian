"""
This file contains a mixins for drawable and animated objects.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/22/20
"""
import pygame

from gale.animation import Animation

import settings


class DrawableMixin:
    def render(self, surface):
        texture = settings.GAME_TEXTURES[self.texture]
        frame = settings.GAME_FRAMES[self.texture][self.frame]
        image = pygame.Surface((frame.width, frame.height), pygame.SRCALPHA)
        image.fill((0, 0, 0, 0))
        image.blit(texture, (0, 0), frame)

        if self.inverted:
            image = pygame.transform.flip(image, True, False)

        surface.blit(image, (self.x, self.y))


class AnimatedMixin:
    def _generate_animations(self, animations):
        for k, v in animations.items():
            animation = Animation(
                v['frames'],
                v.get('interval', 0),  # Given interval or zero
                loops=v.get('loops')   # Given loops or None
            )
            self.animations[k] = animation

    def change_animation(self, animation):
        self.current_animation = self.animations[animation]
        self.current_animation.reset()
        self.frame = self.current_animation.get_current_frame()

    def update(self, dt):
        self.current_animation.update(dt)
        self.frame = self.current_animation.get_current_frame()


class CollisionMixin:
    def get_collision_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def collides(self, another):
        return self.get_collision_rect().colliderect(
            another.get_collision_rect()
        )

    def collision_shifts(self, another):
        r1 = self.get_collision_rect()
        r2 = another.get_collision_rect()

        if (r1.x > r2.right or r1.right < r2.x
                or r1.bottom < r2.y or r1.y > r2.bottom):
            # There is no intersection
            return None

        # Compute x shift
        if r1.centerx < r2.centerx:
            x_shift = r1.right - r2.x
        else:
            x_shift = r1.x - r2.right

        # Compute y shift
        if r1.centery < r2.centery:
            y_shift = r2.y - r1.bottom
        else:
            y_shift = r2.bottom - r1.y

        return x_shift, y_shift
