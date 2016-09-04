
class Player(object):
    def __init__(self):
        self.fireDirection = 0
        self.firing = False
        self.maxlife = 40
        self.laserlife = 0
        self.score = 0

    def fire(self, direction):
        if self.firing:
            return
        self.firing = True
        self.laserlife = 10
        self.fireDirection = direction

    def update(self):
        print(self.firing)
        print(self.laserlife)
        if self.firing:
            self.laserlife -= 1
            if self.laserlife < 0:
                self.firing = False
                self.fireDirection = 0
