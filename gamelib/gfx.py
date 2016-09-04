from pygame.locals import *
import pygame
import pygame.gfxdraw

midpoint = (285, 315)
dpoint = (300, 300)
laserColor = (0, 255, 0)
targets = ((300, 0), (600, 300), (300, 600), (0, 300))

impColors = ((125, 125, 125),(155, 155, 155),)
shipColors = ((0, 255, 0),(0, 155, 0),)

def drawBase(sfc):
    pygame.gfxdraw.filled_circle(sfc, midpoint[0], midpoint[1], 39, impColors[0])
    pygame.gfxdraw.circle(sfc, midpoint[0], midpoint[1], 39, impColors[1])
    pygame.gfxdraw.filled_circle(sfc, dpoint[0], dpoint[1], 8, impColors[1])
    pygame.gfxdraw.filled_circle(sfc, dpoint[0], dpoint[1], 2, impColors[0])
    pygame.gfxdraw.hline(sfc, midpoint[0]-39, midpoint[0]+39, 315, impColors[1])


def drawLaser(sfc, direction):
    pygame.draw.line(sfc, laserColor, dpoint, targets[direction-1])


def drawShip(sfc, event):
    pygame.draw.rect(sfc, shipColors[0], event.body)