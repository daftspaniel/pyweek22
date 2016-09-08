from gamelib.events.gevent import GEvent
import math
from pygame.locals import *
from gamelib.util.gfxutil import *


class Shuttle(GEvent):
    def __init__(self, sole=True):
        super(GEvent, self).__init__()
        self.alive = True
        self.type = 5
        self.sole = sole
        self.shootable = True
        self.width = 30
        self.x = 300
        self.y = 0
        self.stepx = 2
        self.stepy = 2
        self.min = 0
        self.max = 560
        self.invertX = RND(1)
        self.invertY = RND(1)
        if self.invertX == 1:
            self.stepx = -2
        if self.invertY == 1:
            self.stepy = -2

    def IsComplete(self):
        return False if self.alive else True

    def update(self):

        self.x += self.stepx
        self.y += self.stepy
        if self.x < self.min or self.x > self.max:
            self.stepx *= -1
            self.max -= 20
            self.min += 20
            if self.x < self.min: self.x = self.min
            if self.x > self.max: self.x = self.max

        if self.y < self.min or self.y > self.max:
            self.stepy *= -1
            self.min += 20
            self.max -= 20
            if self.y < self.min: self.y = self.min
            if self.y > self.max: self.y = self.max

        if self.min > 200: self.min = 200
        if self.max < 300: self.max = 300

        if self.invertX == 1:
            self.x = 600 - self.x
        if self.invertY == 1:
            self.y = 600 - self.y

        self.body.left = self.x
        self.body.top = self.y

    def setOriginAndSpeed(self, pos, speed):
        halfwidth = int(self.width / 2)
        self.body = Rect(pos[0] - halfwidth, pos[1], self.width, self.width)
        self.vx = speed[0]
        self.vy = speed[1]
        self.x = self.body.left
        self.y = self.body.top
