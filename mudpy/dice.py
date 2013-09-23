from random import randint


class Dice(object):

    def __init__(self, number, sides):
        assert(number > 0)
        assert(sides > 1)
        self.number = number
        self.sides = sides

    def __repr__(self):
        return "%sd%s" % (self.number, self.sides)

    def roll(self):
        return sum([randint(1, self.sides) for _ in xrange(1, self.number)])