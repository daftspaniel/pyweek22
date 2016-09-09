import pygame
from pygame.locals import *
import os

class SFXStore(object):
    def __init__(self):
        self.alert = self.LoadSND("snd/alert.wav")
        self.boom = self.LoadSND("snd/boom.wav")
        self.boom2 = self.LoadSND("snd/boom2.wav")
        self.gameoverboom = self.LoadSND("snd/gameoverboom.wav")
        self.inter = self.LoadSND("snd/inter.wav")
        self.zap = self.LoadSND("snd/zap.wav")

    def LoadSND(self, filename):
        if filename.find(os.sep) == -1:
            filename = filename.replace("/", os.sep)
        return pygame.mixer.Sound(filename)