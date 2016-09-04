print("Please use Python 3 for this game - thanks!")

import pygame
from gamelib.gfxutil import *
from gamelib.zapgame import *
import sys

## GLOBAL SETUP
pygame.init()
ScreenSize = [600, 600]

screen = pygame.display.set_mode(ScreenSize)

pygame.display.set_caption("Zap!")
pygame.key.set_repeat(10, 10)
surface = CreateSurface(screen)
Game = None


# ------
# MAIN
# ------
def main():
    GameState = 2
    surface.fill(pygame.Color("white"))
    DrawText(surface, 10, 50, "Daftspaniel Presents...")
    screen.blit(surface, (0, 0))
    pygame.display.flip()

    while GameState != -1:
        if GameState == 2:
            surface.fill(pygame.Color("black"))

            DrawText(surface, 10, 50, "Please Wait...")
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
