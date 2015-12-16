# coding=utf-8
from Jon import *


class Peptyd(Seq):
    def fragmentuj(self):
        for i in xrange(len(self.seq) + 1):
            self.jony.append(Jony(JonB(self.seq[:i]), JonY(self.seq[i:])))

    def __init__(self, seq):
        super(Peptyd, self).__init__(seq)
        self.jony = []
        self.fragmentuj()
        self.masa = self.policz_mase(self.seq)
        if self.masa > 0:
            self.masa += self.atomy()['H'] + self.atomy()['O'] + self.atomy()['H']

    def __str__(self):
        w = 'Peptyd:\n'
        w += '\tsekwencja[' + str(len(self.seq)) + ']: ' + self.seq + '\n'
        w += '\tmasa: ' + str(self.masa) + '\n'
        w += '\tJony[' + str(len(self.jony)) + ']:\n'
        for jon in self.jony:
            for j in str(jon).split('\n'):
                w += '\t\t' + j + '\n'
        return w[:-1]
