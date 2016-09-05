from gamelib.level import *
from gamelib.gfx import *
from gamelib.ship import *

N = (300, -50)
E = (650, 300)
S = (300, 650)
W = (-50, 300)
TN = (-50, 100)
Directions = (N, S, E, W)
SLOW = 1
MED = 3
FAST = 5
CRAZY = 8

vs = {}
vs['n'] = (0, SLOW * -1)
vs['s'] = (0, SLOW)
vs['e'] = (SLOW, 0)
vs['w'] = (SLOW - 1, 0)


def getRandomDirection():
    return Directions[RND(3)]


def getLevel(index):
    level = []
    if index == 1:
        level.extend([GameText("GET READY!"),
                      Pause(1),
                      TFighter(vs['e'], TN, False),
                      Asteroid(vs['s'], N),
                      Pause(),
                      Ship(vs['n'], S),
                      Ship(vs['e'], W),
                      Ship(vs['w'], E, False),
                      Ship(vs['e'], W),
                      Asteroid((0, FAST), N),
                      Asteroid((0, FAST * -1), S)
                      ])
    return level
