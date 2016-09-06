import pygame.gfxdraw

from gamelib.util.gfxutil import *

midpoint = (285, 315)
dpoint = (300, 300)
laserColor = (0, 255, 0)
targets = ((300, 0), (600, 300), (300, 600), (0, 300))

impColors = ((125, 125, 125), (155, 155, 155),)
shipColors = ((0, 255, 0), (0, 15, 255),)


def drawBase(sfc):
    pygame.gfxdraw.filled_circle(sfc, midpoint[0], midpoint[1], 39, impColors[0])
    pygame.gfxdraw.aacircle(sfc, midpoint[0], midpoint[1], 39, impColors[1])
    pygame.gfxdraw.filled_circle(sfc, dpoint[0], dpoint[1], 8, impColors[1])
    pygame.gfxdraw.filled_circle(sfc, dpoint[0], dpoint[1], 2, impColors[0])
    pygame.gfxdraw.hline(sfc, midpoint[0] - 39, midpoint[0] + 39, 315, impColors[1])


def drawLaser(sfc, direction):
    pygame.draw.line(sfc, laserColor, dpoint, targets[direction - 1])


def drawFighter(sfc, event):
    rt = event.body
    pygame.gfxdraw.vline(sfc, rt.left, rt.top, rt.bottom, impColors[1])
    pygame.gfxdraw.aacircle(sfc, rt.center[0], rt.center[1], 3, impColors[1])
    pygame.gfxdraw.filled_circle(sfc, rt.center[0], rt.center[1], 3, impColors[1])
    pygame.gfxdraw.vline(sfc, rt.left + rt.w, rt.top, rt.bottom, impColors[1])
    pygame.draw.line(sfc, impColors[1], rt.midleft, rt.midright)


def drawAsteroid(sfc, event):
    rt = event.body
    points = [(10, 10), (22, 0), (50, 20), (40, 40), (22, 37), (15, 35)]
    ap = []
    for point in points:
        ap.append([point[0] + rt.left, point[1] + rt.top])
    pygame.gfxdraw.filled_polygon(sfc, ap, (255, 111, 51))


def drawShip(sfc, event):
    rt = event.body

    pygame.draw.line(sfc, shipColors[1], rt.topleft, rt.bottomright)
    pygame.draw.line(sfc, shipColors[1], rt.topright, rt.bottomleft)
    pygame.gfxdraw.filled_circle(sfc, rt.topleft[0], rt.topleft[1], 2, (255, 255, 255))
    pygame.gfxdraw.filled_circle(sfc, rt.bottomright[0], rt.bottomright[1], 2, (255, 255, 255))
    pygame.gfxdraw.filled_circle(sfc, rt.topright[0], rt.topright[1], 2, (255, 255, 255))
    pygame.gfxdraw.filled_circle(sfc, rt.bottomleft[0], rt.bottomleft[1], 2, (255, 255, 255))

    pygame.gfxdraw.filled_circle(sfc, rt.center[0], rt.center[1], 8, (255, 255, 255))
    pygame.gfxdraw.aacircle(sfc, rt.center[0], rt.center[1], 8, shipColors[1])


def drawTxt(sfc, event):
    drawText(sfc, event.body.left, event.body.top, event.text, 24, (255, 255, 255))
