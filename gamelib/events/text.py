from gamelib.events.pause import Pause

class Text(Pause):
    def __init__(self, text="hello world", duration=12, sole=True):
        super(Text, self).__init__(duration)

        self.text = text
        self.type = 2
        self.shootable = False
        self.sole = sole

    def update(self):
        self.life -= 1
        self.body.left += 5