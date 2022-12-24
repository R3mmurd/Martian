"""
This file contains the implementation of the game states.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/19/2020
"""
import pygame

from gale.animation import Animation
from gale.state_machine import BaseState
from gale.text import Text, render_text
from gale.timer import Timer

from src.player import Player
from src.game_level import GameLevel

from src.defs.items import ITEMS

import settings


class StartState(BaseState):
    def enter(self):
        pygame.mixer_music.load('sounds/music_intro.ogg')
        pygame.mixer_music.play(loops=-1)

        self.title = Text(
            'Super Martian', settings.GAME_FONTS['medium'],
            settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT//4,
            (197, 195, 198), shadowed=True
        )
        
        self.x = -settings.PLAYER_WIDTH
        self.texture = settings.GAME_TEXTURES['martian']
        self.animation = Animation(
            settings.GAME_FRAMES['martian'][9:], 0.15
        )
        
        self.can_input = False
    
        def arrive():
            self.can_input = True
            self.animation = Animation(
                [settings.GAME_FRAMES['martian'][0]],
            )

        Timer.tween(
            5,
            [
                (self.title, {'x': settings.VIRTUAL_WIDTH//2 - self.title.rect.width//2}),
                (self, {'x': settings.VIRTUAL_WIDTH//2 - 8})
            ],
            on_finish=arrive
        )        
    
    def update(self, dt):
        self.animation.update(dt)

        if self.can_input and settings.pressed_keys.get(pygame.K_RETURN):
            pygame.mixer_music.stop()
            self.state_machine.change('play')
    
    def render(self, surface):
        surface.fill((25, 130, 196))
        self.title.render(surface)
        surface.blit(
            self.texture, (self.x, settings.VIRTUAL_HEIGHT//2-10),
            self.animation.get_current_frame()
        )

        if self.can_input:
            render_text(
                surface, 'Press Enter!', settings.GAME_FONTS['small'],
                settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//2+40,
                (197, 195, 198), center=True, shadowed=True
            )


class PlayState(BaseState):
    def enter(self):
        pygame.mixer_music.load('sounds/music_grassland.ogg')
        pygame.mixer_music.play(loops=-1)
        self.game_level = GameLevel(level=1)
        self.tile_map = self.game_level.tile_map
        self.player = Player(16, 16*5, self.game_level)
        self.player.change_state('fall')
        self.time = 30

        def dec_time():
            self.time -= 1

            if 0 <= self.time < 5:
                settings.GAME_SOUNDS['timer'].play()

        self.timer = Timer.every(1, dec_time, limit=self.time + 1)
        self.timer.finish(
            lambda: self.state_machine.change('stats', self.player)
        )

    def exit(self):
        pygame.mixer_music.stop()

    def update(self, dt):
        if self.player.dead:
            self.timer.remove()
            self.state_machine.change('stats', self.player)

        self.player.update(dt)

        if self.player.y > settings.VIRTUAL_HEIGHT:
            self.player.dead = True

        for enemy in self.game_level.enemies:
            enemy.update(dt)

            if self.player.collides(enemy):
                self.player.dead = True

        for item in self.game_level.items:
            if not item.in_play or not item.collidable:
                continue

            if self.player.collides(item):
                item.on_collide(self.player)

                if item.consumable:
                    item.on_consume(self.player)

    def render(self, surface):
        shift_x = max(
            min(0, settings.VIRTUAL_WIDTH//2 - int(self.player.x+8)),
            -(self.tile_map.width - settings.VIRTUAL_WIDTH)
        )
        world_canvas = pygame.Surface(
            (self.tile_map.width, self.tile_map.height)
        )
        self.game_level.render(world_canvas)
        self.player.render(world_canvas)

        surface.blit(world_canvas, (shift_x, 0))

        render_text(
            surface, f'Score: {self.player.score}',
            settings.GAME_FONTS['small'], 5, 5, (255, 255, 255),
            shadowed=True
        )
        render_text(
            surface, f'Time: {self.time}',
            settings.GAME_FONTS['small'], settings.VIRTUAL_WIDTH-60, 5,
            (255, 255, 255), shadowed=True
        )


class StatsState(BaseState):
    def enter(self, player):
        self.player = player
        self.coin_defs = ITEMS['coin']

    def update(self, dt):
        if settings.pressed_keys.get(pygame.K_RETURN):
            self.state_machine.change('play')

    def render(self, surface):
        surface.fill((25, 130, 196))

        render_text(
            surface, 'Game Over!', settings.GAME_FONTS['medium'],
            settings.VIRTUAL_WIDTH // 2, 20,
            (255, 255, 255), center=True, shadowed=True
        )

        y = 50

        for color, number in self.player.coin_counter.items():
            surface.blit(
                settings.GAME_TEXTURES['tiles'],
                (settings.VIRTUAL_WIDTH//2 - 32, y),
                settings.GAME_FRAMES['tiles'][self.coin_defs['frame'][color]]
            )
            render_text(
                surface, 'x', settings.GAME_FONTS['small'],
                settings.VIRTUAL_WIDTH//2, y + 3, (255, 255, 255),
                shadowed=True
            )
            render_text(
                surface, f'{number}', settings.GAME_FONTS['small'],
                settings.VIRTUAL_WIDTH // 2 + 16, y + 3, (255, 255, 255),
                shadowed=True
            )
            y += 20

        render_text(
            surface, f'Score: {self.player.score}', settings.GAME_FONTS['small'],
            settings.VIRTUAL_WIDTH//2, y+10, (255, 255, 255),
            shadowed=True, center=True
        )

        render_text(
            surface, 'Press Enter to play again!', settings.GAME_FONTS['small'],
            settings.VIRTUAL_WIDTH // 2, settings.VIRTUAL_HEIGHT - 20,
            (255, 255, 255), center=True, shadowed=True
        )

