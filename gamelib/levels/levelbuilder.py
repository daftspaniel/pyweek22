from gamelib.events.asteroid import *
from gamelib.events.ship import *
from gamelib.events.pause import *
from gamelib.events.text import *
from gamelib.events.tfighter import *
from gamelib.events.shuttle import *
from gamelib.levels.directions import *


def setNSEW(level, event, sole=True):
    level.extend([N(event(sole)),
                  S(event(sole)),
                  E(event(sole)),
                  W(event(sole))])


def getLevel(index):
    level = []
    if index == 1:
        setNSEW(level, TFighter, False)

        level.extend([Text("GET READY!"),
                      Pause(4)])

        level.extend([Pause(1),
                      R(Ship()),
                      R(Ship()),
                      R(Ship()),
                      R(Ship())])

        level.extend([E(Asteroid(False)),
                      W(Asteroid()),
                      N(Ship(False)),
                      W(Ship()),
                      E(Ship()),
                      W(Ship(False)),
                      S(Ship()),
                      R(Ship()),
                      R(Asteroid(False)),
                      Pause(2),
                      N(Shuttle()),
                      R(Ship(False)),
                      Pause(2)
                      ])

        setNSEW(level, TFighter, False)

        level.extend([Pause(4), Text("LEVEL UP", 12, True)])

        speedUp()

        setNSEW(level, Asteroid, False)

        level.extend([Pause(3)])

        level.extend([
            E(Ship(False)),
            Pause(3),
            S(Ship(False)),
            Pause(2),
            W(Asteroid(False))
        ])

        level.append(R(Ship(False)))
        level.append(R(Ship(False)))
        level.append(R(Ship(False)))
        level.append(R(Ship(False)))

        level.append(Pause(10))

        setNSEW(level, Asteroid, False)
        setNSEW(level, Shuttle, False)
        setNSEW(level, Ship, True)


    return level
