from gamelib.events.gevent import GEvent
from gamelib.util.gfxutil import *
import pygame
from pygame.locals import *

class TFighter(GEvent):
    def __init__(self, sole=False):
        super(TFighter, self).__init__()
        self.alive = True
        self.type = 4
        self.sole = sole
        self.shootable = False

    def IsComplete(self):
        if abs(self.body.left)+abs(self.body.top) >1200:
            self.alive = False
        return False if self.alive else True

    def setOriginAndSpeed(self, pos, speed):
        halfwidth = int(self.width / 2)
        self.body = Rect(pos[0] - halfwidth, pos[1], self.width, self.width)
        self.vx = speed[0]
        self.vy = speed[1]
        if self.vx == 0: self.body.left += -40 + RND(90)
        if self.vy == 0: self.body.top += -40 + RND(90)

