import pygame
from pygame.locals import *

class GEvent(object):

    def __init__(self):
        self.shootable = False
        self.body = Rect(0, 0, 0, 0)
        self.vx = 0
        self.vy = 0
        self.width = 30

    def IsComplete(self):
        pass

    def setOriginAndSpeed(self, pos, speed):
        halfwidth = int(self.width / 2)
        self.body = Rect(pos[0] - halfwidth, pos[1], self.width, self.width)
        self.vx = speed[0]
        self.vy = speed[1]

    def update(self):
        self.body.left += self.vx
        self.body.top += self.vy
