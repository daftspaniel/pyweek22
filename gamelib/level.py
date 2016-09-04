from gamelib.logger import *

class Level(object):
    def __init__(self, events):
        self.happenings = events

    def getNext(self):
        pass


class Levels(object):
    def __init__(self, levels):
        self.levels = levels
        self.event = self.levels[0]

    def update(self):

        if self.event.IsComplete():
            if len(self.levels) > 0:
                self.event = self.levels.pop(0)
            else:
                self.event = Pause(4)
        else:
            self.event.update()


class GameEvent(object):
    def __init__(self):
        pass

    def IsComplete(self):
        pass

class Pause(GameEvent):
    def __init__(self, duration=5):
        self.life = duration * 25
        self.type = 0
    def update(self):
        #log(self.life)
        self.life -= 1

    def IsComplete(self):
        return False if self.life > 0 else True
