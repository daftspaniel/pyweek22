from gamelib.level import *
from gamelib.gfx import *
from gamelib.ship import *

N = (300, -50)
E = (650, 300)
S = (300, 650)
W = (-50, 300)

Directions = (N, S, E, W)
SLOW = 3
MED = 5
FAST = 7
CRAZY = 8

def getRandomDirection():
    return Directions[RND(3)]


def getLevel(index):
    level = []
    if index == 1:
        level.extend([GameText("GET READY!"),
                      Pause(3),
                      Ship((0, SLOW), N),
                      Pause(),
                      Ship((0, SLOW * -1), S),
                      Pause(),
                      Ship((SLOW, 0), W),
                      Pause(),
                      Ship((SLOW * -1, 0), E),
                      ])
        print(level)
    return level
