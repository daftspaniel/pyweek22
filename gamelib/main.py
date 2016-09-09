print("Please use Python 3 for this game - thanks!")

from gamelib.zapgame import *
from gamelib.util.gfxutil import *
from gamelib.gfx.gfx import *
from gamelib.util.snd import *

## GLOBAL SETUP
pygame.init()
ScreenSize = [600, 600]

screen = pygame.display.set_mode(ScreenSize)

pygame.display.set_caption("Zap!")
pygame.key.set_repeat(10, 10)
surface = createSurface(screen)
Game = None

starfields = [
    Starfield((0, 0), (600, 600), 20, 1),
    Starfield((0, 0), (600, 600), 30, 2),
    Starfield((0, 0), (600, 600), 40, 3)
]

starfields[0].color = (255, 0, 0)
starfields[1].color = (0, 255, 0)
starfields[2].color = (0, 0, 255)


# ------
# MAIN
# ------
def main():
    sfx = SFXStore()
    sfx.inter.play()
    GameState = 1
    surface.fill(pygame.Color("white"))
    drawText(surface, 10, 50, "Daftspaniel Presents...")
    screen.blit(surface, (0, 0))
    pygame.display.flip()
    sfx.inter.play()

    while GameState != -1:
        if GameState == 1:
            sfx.inter.play()
            surface.fill(pygame.Color("black"))
            drawText(surface, 10, 50, "Space Station",48)

            p1 = "Defend the Spacestation from the terrorist forces"
            p2 = "using WASD to fire lasers up, down, left and right."
            p3 = "The battle will get increasingly intense!"
            p4 = "If the space station is too damaged, then the"
            p5 = "Reg5 bomber will finish the outpost off"
            p6 = "Don't Let Him In!"
            drawText(surface, 10, 150, p1)
            drawText(surface, 10, 180, p2)
            drawText(surface, 10, 220, p3)
            drawText(surface, 10, 350, p4)
            drawText(surface, 10, 370, p5)
            drawText(surface, 10, 400, p6, 40, (255,0,0))

            drawText(surface, 10, 580, "Press spacebar to begin!")

            global starfields
            for s in starfields:
                s.update()
                s.draw(surface)
            screen.blit(surface, (0, 0))
            pygame.display.flip()
            while GameState == 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                    elif event.type == KEYDOWN:
                        keystate = pygame.key.get_pressed()

                        if keystate[K_SPACE] == 1:
                            GameState = 2

        elif GameState == 2:
            sfx.boom2.play()
            surface.fill(pygame.Color("black"))

            drawText(surface, 10, 50, "Please Wait...")
            screen.blit(surface, (0, 0))
            pygame.display.flip()
            Game = ZapGame(surface, screen)
            surface.fill(pygame.Color("black"))
            GameState = 3

        elif GameState == 3:
            surface.fill(pygame.Color("blue"))
            screen.blit(surface, (0, 0))
            pygame.display.flip()
            while GameState == 3:
                Game.MainLoop()
                GameState = 4
