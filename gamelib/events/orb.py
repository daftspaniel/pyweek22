from gamelib.events.gevent import GEvent

class Orb(GEvent):
    def __init__(self, sole=True):
        super(GEvent, self).__init__()
        self.alive = True
        self.type = 6
        self.sole = sole
        self.shootable = True
        self.width = 3

    def IsComplete(self):
        return False if self.alive else True

    def update(self):
        self.body.left += self.vx
        self.body.top += self.vy