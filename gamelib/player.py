from pygame.locals import *
import pygame
import pygame.gfxdraw
from gamelib.logger import *

class Player(object):
    def __init__(self):
        self.fireDirection = 0
        self.firing = False
        self.maxlife = 10
        self.laserlife = 0
        self.score = 0
        self.laserPos = [Rect(299,0,3,300),Rect(300,299,300,3),Rect(299,300,3,300),Rect(0,299,300,3)]

    def fire(self, direction):
        if self.firing:
            return
        self.firing = True
        self.laserlife = self.maxlife
        self.fireDirection = direction

    def update(self):
        log(self.firing)
        log(self.laserlife)
        if self.firing:
            self.laserlife -= 1
            if self.laserlife < 0:
                self.firing = False
                self.fireDirection = 0

    def getLaserRects(self):
        return self.laserPos[self.fireDirection-1]
