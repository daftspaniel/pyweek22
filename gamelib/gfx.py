from pygame.locals import *
import pygame
import pygame.gfxdraw
from gamelib.gfxutil import *

midpoint = (285, 315)
dpoint = (300, 300)
laserColor = (0, 255, 0)
targets = ((300, 0), (600, 300), (300, 600), (0, 300))

impColors = ((125, 125, 125),(155, 155, 155),)
shipColors = ((0, 255, 0),(0, 15, 255),)

def drawBase(sfc):
    pygame.gfxdraw.filled_circle(sfc, midpoint[0], midpoint[1], 39, impColors[0])
    pygame.gfxdraw.circle(sfc, midpoint[0], midpoint[1], 39, impColors[1])
    pygame.gfxdraw.filled_circle(sfc, dpoint[0], dpoint[1], 8, impColors[1])
    pygame.gfxdraw.filled_circle(sfc, dpoint[0], dpoint[1], 2, impColors[0])
    pygame.gfxdraw.hline(sfc, midpoint[0]-39, midpoint[0]+39, 315, impColors[1])


def drawLaser(sfc, direction):
    pygame.draw.line(sfc, laserColor, dpoint, targets[direction-1])


def drawShip(sfc, event):
    rt = event.body
    pygame.draw.line(sfc, shipColors[1], rt.topleft, rt.bottomright)
    pygame.draw.line(sfc, shipColors[1], rt.topright, rt.bottomleft)
    pygame.gfxdraw.circle(sfc, rt.center[0],rt.center[1], 8, shipColors[1])

def drawTxt(sfc, event):
    drawText(sfc, event.body.left, event.body.top, event.text, 24, (255, 255, 255))