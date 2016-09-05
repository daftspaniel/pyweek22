from pygame.locals import *
from gamelib.logger import *


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

        #print("self.levels" + str(len(self.levels)))
        #for event in self.levels:
        while len(self.levels)>0 and (len(self.events)==0 or self.events[-1].sole == False):
            self.events.append(self.levels.pop(0))
            #print("Added" + str(self.events[-1]))
            #print(event.sole)
            #if event.sole == True:
            #    print("BREAK")
            #    break
        #print(len(self.events))

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


class GameEvent(object):
    shootable = False

    def __init__(self):
        pass

    def IsComplete(self):
        pass


class Pause(GameEvent):
    def __init__(self, duration=1):
        self.life = duration * 10
        self.type = 0
        self.sole = True

    def update(self):
        self.life -= 1

    def IsComplete(self):
        return False if self.life > 0 else True


class GameText(Pause):
    def __init__(self, text="hello world", duration=10, pos=(0, 0)):
        super(GameText, self).__init__(duration)
        self.body = Rect(pos[0], pos[1], 300, 50)
        self.text = text
        self.type = 2
        self.shootable = False
