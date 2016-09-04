import random
import pygame




def RND(maxv):
    return random.randrange(0, maxv)


def CreateSurface(screen):
    bg = pygame.Surface(screen.get_size())
    bg = bg.convert()
    return bg


def DrawText(bg, x, y, text, size=24, color=(255, 255, 255)):
    inst1_font = pygame.font.Font(None, size)
    inst1_surf = inst1_font.render(text, 1, color)
    bg.blit(inst1_surf, [x, y])
