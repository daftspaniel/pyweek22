from pygame.locals import *
import pygame
import pygame.gfxdraw
from gamelib.level import *


class Ship(GameEvent):
    def __init__(self, vector=(0, 1), pos=(285, 0), sole=True):
        self.alive = True
        self.type = 1
        self.body = Rect(pos[0], pos[1], 30, 30)
        self.vy = vector[1]
        self.vx = vector[0]
        self.sole = sole
        self.shootable = True

    def update(self):
        self.body.left += self.vx
        self.body.top += self.vy

    def IsComplete(self):
        return False if self.alive else True
