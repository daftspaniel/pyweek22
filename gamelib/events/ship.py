from gamelib.events.gevent import GEvent

class Ship(GEvent):
    def __init__(self, sole=True):
        super(GEvent, self).__init__()
        self.alive = True
        self.type = 1
        self.sole = sole
        self.shootable = True
        self.width = 30

    def IsComplete(self):
        return False if self.alive else True

    def update(self):
        self.body.left += self.vx
        self.body.top += self.vy