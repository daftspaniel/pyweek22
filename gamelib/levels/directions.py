from gamelib.gfx import *
from gamelib.util.gfxutil import *

NORTH = (300, -50)
EAST = (650, 300)
SOUTH = (300, 650)
WEST = (-50, 300)
TN = (-50, 100)

SLOW = 2
MED = 3
FAST = 5
CRAZY = 8

vs = {}
vs['n'] = (0, SLOW* -1)
vs['s'] = (0, SLOW)
vs['e'] = (SLOW, 0)
vs['w'] = (SLOW * - 1, 0)

ms = {}
ms['n'] = (0, MED* -1)
ms['s'] = (0, MED)
ms['e'] = (MED, 0)
ms['w'] = (MED * - 1, 0)

Directions = (NORTH, SOUTH, EAST, WEST)
Speeds = (vs['s'], vs['n'], vs['w'], vs['e'])

def speedUp():
   global vs
   vs['n'] = (0, MED * -1)
   vs['s'] = (0, MED)
   vs['e'] = (MED, 0)
   vs['w'] = (MED * - 1, 0)


def N(event):
    event.setOriginAndSpeed(NORTH, vs['s'])
    return event


def S(event):
    event.setOriginAndSpeed(SOUTH, vs['n'])
    return event


def E(event):
    event.setOriginAndSpeed(EAST, vs['w'])
    return event


def W(event):
    event.setOriginAndSpeed(WEST, vs['e'])
    return event


def R(event):
    i = RND(3)
    event.setOriginAndSpeed(Directions[i], Speeds[i])
    return event
