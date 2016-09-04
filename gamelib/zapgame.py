import pygame
from pygame.locals import *
from gamelib.gfxutil import *
from gamelib.player import *
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

    def MainLoop(self):
        #
        self.UpdateScreen()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                elif event.type == KEYDOWN:
                    keystate = pygame.key.get_pressed()

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
                    self.UpdateScreen()
                    self.screen.blit(self.surface, (0, 0))
                    pygame.display.flip()

    def UpdateScreen(self):
        self.surface.fill((0,0,0))
        print("Game ON..." + str(self.p1.fireDirection))
        DrawText(self.surface, 10, 50, "Game ON..." + str(self.p1.fireDirection))

        self.drawLaser()

        pygame.draw.circle(self.surface, (0, 255, 0), (300, 300), 30)

    def drawLaser(self):
        if self.p1.fireDirection == 3:
            pygame.draw.line(self.surface, (255, 0, 0), (300, 300), (300, 600))
        elif self.p1.fireDirection == 4:
            pygame.draw.line(self.surface, (255, 0, 0), (300, 300), (0, 300))
        elif self.p1.fireDirection == 1:
            pygame.draw.line(self.surface, (255, 0, 0), (300, 300), (300,0))
        elif self.p1.fireDirection == 2:
            pygame.draw.line(self.surface, (255, 0, 0), (300, 300), (600,300))
