import pygame
from pygame.locals import *
from gamelib.util.logger import *


class Player(object):
    def __init__(self):
        self.fireDirection = 0
        self.firing = False
        self.maxlife = 5
        self.laserlife = 0
        self.score = 0
        self.shields = 100
        self.damage = []
        self.laserPos = [Rect(299, 0, 3, 300), Rect(300, 299, 300, 3), Rect(299, 300, 3, 300), Rect(0, 299, 300, 3)]
        self.shots = 0
        self.hits = 0

    def fire(self, direction):
        if self.firing:
            return
        self.sfx.zap.play()
        self.firing = True
        self.laserlife = self.maxlife
        self.fireDirection = direction
        self.shots += 1

    def update(self):
        log(self.firing)
        log(self.laserlife)
        if self.firing:
            self.laserlife -= 1
            if self.laserlife < 0:
                self.firing = False
                self.fireDirection = 0

    def getLaserRects(self):
        return self.laserPos[self.fireDirection - 1]
