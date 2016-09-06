from gamelib.events.gevent import GEvent

class Shuttle(GEvent):
    def __init__(self, sole=True):
        super(GEvent, self).__init__()
        self.alive = True
        self.type = 5
        self.sole = sole
        self.shootable = True
        self.width = 30

    def IsComplete(self):
        return False if self.alive else True
