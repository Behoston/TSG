# coding=utf-8
from Seq import Seq


class Jon(Seq):
    def __init__(self, seq):
        super(Jon, self).__init__(seq)

    def __str__(self):
        w = type(self).__name__ + ': \n'
        w += '\tsekwencja[' + str(len(self.seq)) + ']: ' + self.seq + '\n'
        w += '\tmasa: ' + str(self.masa)
        return w


class JonB(Jon):
    """ zawiera dodatkowy H """

    def __init__(self, seq):
        super(JonB, self).__init__(seq)
        if self.masa > 0:
            self.masa += self.atomy()['H']


class JonY(Jon):
    """ zawiera dodatkową grupę OH """

    def __init__(self, seq):
        super(JonY, self).__init__(seq)
        if self.masa > 0:
            self.masa += self.atomy()['H'] + self.atomy()['O']


class Jony(object):
    def __init__(self, b, y):
        super(Jony, self).__init__()
        self.b = b
        self.y = y

    def __repr__(self):
        return 'Jony(' + self.b.__repr__() + ', ' + self.y.__repr__() + ')'

    def __str__(self):
        w = 'Jony:\n'
        for b in str(self.b).split('\n'):
            w += '\t' + b + '\n'
        for y in str(self.y).split('\n'):
            w += '\t' + y + '\n'
        return w[:-1]
