from pygame.locals import *
import pygame
import pygame.gfxdraw


class Ship():
    def __init__(self, vector=(0, 1), pos=(285, 0)):
        self.alive = True
        self.type = 1

        self.vy = vector[1]
        self.vx = vector[0]
        self.body = Rect(pos[0], pos[1], 30, 30)

    def update(self):
        self.body.left += self.vx
        self.body.top += self.vy

    def IsComplete(self):
        return False if self.alive else True
