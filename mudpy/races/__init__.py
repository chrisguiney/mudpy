__author__ = 'chris'


class Race(object):
    attributes = {
        "strength": 9,
        "dexterity": 9,
        "wisdom": 9,
        "intelligence": 9,
        "charisma": 9
    }

    bonuses = {}


class Human(Race):
    pass

class Elf(Race):
    bonuses = {
        "dexterity": {
            "value": 2,
            "description": "Elves are nimble, and quick, and can walk on snow"
        }
    }

class Orc(Race):
    bonuses = {
        "strength": {
            "value": 2,
            "description": "Orcs are strong! GRRR!"
        }
    }


def raise_invalid_race(name):
    raise TypeError("%s is not a valid race" % name)