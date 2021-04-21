"""
This file contains the implementation of the class GameObject.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/22/20
"""
from src.mixins import DrawableMixin, CollisionMixin


class GameObject(DrawableMixin, CollisionMixin):
    # Object sides
    TOP = 'top'
    RIGHT = 'right'
    BOTTOM = 'bottom'
    LEFT = 'left'

    def __init__(self, x, y, width, height, texture, frame, solidness):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.texture = texture
        self.frame = frame
        self.solidness = solidness
        self.inverted = False
