from gamelib.events.gevent import GEvent

class Asteroid(GEvent):
    def __init__(self, sole=True):
        super(GEvent, self).__init__()
        self.alive = True
        self.type = 3
        self.sole = sole
        self.shootable = True
        self.width = 30

    def update(self):
        self.body.left += self.vx
        self.body.top += self.vy

    def IsComplete(self):
        return False if self.alive else True