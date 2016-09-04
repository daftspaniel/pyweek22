import pygame
from pygame.locals import *
from gamelib.gfxutil import *
from gamelib.player import *
from gamelib.level import *
from gamelib.gfx import *

ANIMEVENT = pygame.USEREVENT + 3
FPS = 25
pygame.time.set_timer(ANIMEVENT, int(1000 / FPS))


class ZapGame(object):
    """
        Main game class.
    """

    def __init__(self, surface, screen):
        self.surface = surface
        self.screen = screen
        self.p1 = Player()
        self.levels = Levels([Pause(4)])

    def MainLoop(self):
        #
        self.UpdateScreen()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                elif event.type == KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    print("keystate" + str(keystate[K_w]))
                    if keystate[K_w] == 1:
                        self.p1.fire(1)
                    elif keystate[K_d] == 1:
                        self.p1.fire(2)
                    elif keystate[K_s] == 1:
                        self.p1.fire(3)
                    elif keystate[K_a] == 1:
                        self.p1.fire(4)
                elif event.type == ANIMEVENT:
                    self.p1.update()
                    self.levels.update()
                    self.UpdateScreen()
                    self.screen.blit(self.surface, (0, 0))
                    pygame.display.flip()

    def UpdateScreen(self):
        self.surface.fill((0, 0, 0))
        print("Game ON..." + str(self.p1.fireDirection))
        DrawText(self.surface, 10, 50, "Game ON..." + str(self.p1.fireDirection))

        drawBase(self.surface)
        if self.p1.firing: drawLaser(self.surface, self.p1.fireDirection)
