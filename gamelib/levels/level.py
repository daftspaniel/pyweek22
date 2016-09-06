import pygame
from pygame.locals import *

class Level(object):
    def __init__(self, events):
        self.happenings = events

    def getNext(self):
        pass


class LevelFactory(object):
    def __init__(self, levels):
        self.levels = levels
        self.events = []
        self.buildCurrentEvents()

    def buildCurrentEvents(self):
        if len(self.levels) == 0:
            return
        elif len(self.events) > 0 and self.events[-1].sole == True:
            return

        while len(self.levels) > 0 and (len(self.events) == 0 or self.events[-1].sole == False):
            self.events.append(self.levels.pop(0))

    def update(self):
        refreshedEvents = []
        for event in self.events:
            event.update()

        for event in self.events:
            if not event.IsComplete():
                refreshedEvents.append(event)
        count = len(self.events)
        self.events = refreshedEvents

        if count > len(self.events):
            self.buildCurrentEvents()



