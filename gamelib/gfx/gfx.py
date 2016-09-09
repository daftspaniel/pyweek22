import pygame.gfxdraw

from gamelib.util.gfxutil import *

midpoint = (285, 315)
dpoint = (300, 300)
laserColor = (0, 255, 0)
targets = ((300, 0), (600, 300), (300, 600), (0, 300))

impColors = ((125, 125, 125), (155, 155, 155), (195, 195, 195))
shipColors = ((0, 255, 0), (0, 15, 255),)
orbColors = [(51, 196, 155), (51, 196, 255), (251, 196, 155)]
TEXT_COLOR = (255, 255, 128)


def drawBaseExp(sfc,i):
    pygame.gfxdraw.filled_circle(sfc, midpoint[0], midpoint[1], i, (RND(255),0,0))

def drawBase(sfc, damage):
    pygame.gfxdraw.filled_circle(sfc, midpoint[0], midpoint[1], 39, impColors[0])
    pygame.gfxdraw.aacircle(sfc, midpoint[0], midpoint[1], 39, impColors[2])

    for dmg in damage:
        pygame.gfxdraw.filled_circle(sfc, 260 + dmg[0], 260 + dmg[1], dmg[2], (0, 0, 0))

    pygame.gfxdraw.filled_circle(sfc, dpoint[0], dpoint[1], 8, impColors[1])
    pygame.gfxdraw.filled_circle(sfc, dpoint[0], dpoint[1], 2, impColors[0])
    pygame.gfxdraw.hline(sfc, midpoint[0] - 39, midpoint[0] + 39, 315, impColors[1])


def drawOrb(sfc, event):
    rt = event.body
    pygame.gfxdraw.aacircle(sfc, rt.center[0], rt.center[1], 3, orbColors[RND(3) - 1])


def drawLaser(sfc, direction):
    pygame.draw.line(sfc, laserColor, dpoint, targets[direction - 1])
    t = targets[direction - 1]
    if t[1] == 300:
        lt = (t[0], t[1] - 2)
        rt = (t[0], t[1] + 2)
    else:
        lt = (t[0] - 3, t[1])
        rt = (t[0] + 3, t[1])
    points = [dpoint, lt, rt, dpoint]
    pygame.gfxdraw.filled_polygon(sfc, points, laserColor)


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


def drawShuttle(sfc, event):
    rt = event.body
    points = [(15, 0), (15, 15), (30, 30), (15, 15), (0, 30), (15, 15)]
    ap = []
    for point in points:
        ap.append([point[0] + rt.left, point[1] + rt.top])
    pygame.gfxdraw.filled_polygon(sfc, ap, (255, 111, 51))
    pygame.gfxdraw.filled_circle(sfc, rt.center[0], rt.center[1], 4, (0, 0, 255))


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


def drawExplosions(sfc, explosions):
    ne = []
    for e in explosions:
        e[1] -= 1
        if e[1] > 3: ne.append(e)
        pygame.gfxdraw.aacircle(sfc, e[0].center[0], e[0].center[1], e[1]//2, (128 + RND(127), 0, 0))
    return ne


def drawTxt(sfc, event, col=TEXT_COLOR):
    drawText(sfc, event.body.left, event.body.top, event.text, 24, col)


def drawPlayerStatus(sfc, p1):
    drawText(sfc, 5, 4, ("0000" + str(p1.score))[-8:], 24, TEXT_COLOR)
    drawText(sfc, 495, 4, "Shields : " + str(p1.shields), 24, TEXT_COLOR)
    drawText(sfc, 5, 574, ("0000" + str(p1.score))[-8:], 24, TEXT_COLOR)
    drawText(sfc, 415, 574, "Shots/Hits : " + str(p1.hits) + "/" + str(p1.shots), 24, TEXT_COLOR)
