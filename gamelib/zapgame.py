import math

from gamelib.gfx.gfx import *
from gamelib.levels.levelbuilder import *
from gamelib.levels.level import *
from gamelib.player import *

ANIMEVENT = pygame.USEREVENT + 3
FPS = 50
pygame.time.set_timer(ANIMEVENT, int(1000 / FPS))


class ZapGame(object):
    def __init__(self, surface, screen):
        self.surface = surface
        self.screen = screen
        self.p1 = Player()
        self.levels = LevelFactory(getLevel(1))
        self.flash = False

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
                    self.levels.update()
                    self.checkCollisions()
                    self.UpdateScreen()
                    if self.flash:
                        self.surface.fill((255, 0, 0))
                        self.flash = False

                    self.screen.blit(self.surface, (0, 0))
                    pygame.display.flip()

    def UpdateScreen(self):

        self.drawScreenFurniture()

        if self.p1.firing: drawLaser(self.surface, self.p1.fireDirection)

        self.drawShips()

        drawPlayerStatus(self.surface, self.p1)

    def drawShips(self):
        for gameEvent in self.levels.events:

            if gameEvent.type == 1:
                drawShip(self.surface, gameEvent)

            elif gameEvent.type == 2:
                drawTxt(self.surface, gameEvent)

            elif gameEvent.type == 3:
                drawAsteroid(self.surface, gameEvent)

            elif gameEvent.type == 4:
                drawFighter(self.surface, gameEvent)

            elif gameEvent.type == 5:
                drawShuttle(self.surface, gameEvent)

    def drawScreenFurniture(self):
        self.surface.fill((0, 0, 0))
        drawBase(self.surface, self.p1.damage)

    def checkCollisions(self):

        for ship in self.levels.events:
            if ship.shootable:
                if self.p1.firing:
                    self.checkPlayerShots(ship)

                self.checkEnemyCollsion(ship)

    def checkEnemyCollsion(self, ship):
        if math.hypot(ship.body.center[0] - 300, ship.body.center[1] - 300) < 45:
            ship.alive = False
            self.p1.damage.append((RND(70), RND(70), 4 + RND(8)))
            self.p1.shields -= 25
            self.flash = True

    def checkPlayerShots(self, ship):
        centre = ship.body.center
        if ship.body.colliderect(self.p1.getLaserRects()):
            dist = 5 + math.floor(abs(math.hypot(ship.body.center[0] - 300, ship.body.center[1] - 300)) / 10)
            ship.alive = False
            self.p1.score += dist
