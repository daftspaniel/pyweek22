from gamelib.events.gevent import GEvent

class Pause(GEvent):
    def __init__(self, duration=1):
        super(Pause, self).__init__()
        self.life = duration * 10
        self.type = 0
        self.sole = True

    def update(self):
        self.life -= 1

    def IsComplete(self):
        return False if self.life > 0 else True
