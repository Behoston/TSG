# coding=utf-8
from Seq import Seq
from Peptyd import Peptyd


class Bialko(Seq):
    def potnij(self):
        wyniki = []
        peptyd = ''
        for i in self.seq:
            peptyd += i
            if peptyd[-1] == 'K' or peptyd[-1] == 'R':
                wyniki.append(Peptyd(peptyd))
                peptyd = ''
        if wyniki:
            return wyniki
        else:
            return [Peptyd(self.seq)]

    def __init__(self, seq, header):
        super(Bialko, self).__init__(seq)
        self.header = header
        self.masa = self.policz_mase(self.seq)
        if self.masa > 0:
            self.masa += 2 * self.atomy()['H'] + self.atomy()['O']
        self.peptydy = self.potnij()

    def __str__(self):
        w = 'Białko:\n'
        w += '\tnazwa: ' + self.header.strip() + '\n'
        w += '\tsekwencja[' + str(len(self.seq)) + ']: ' + self.seq + '\n'
        w += '\tmasa: ' + str(self.masa) + '\n'
        w += '\tPeptydy [' + str(len(self.peptydy)) + ']:\n'
        for peptyd in self.peptydy:
            for pw in str(peptyd).split('\n'):
                w += '\t\t' + pw + '\n'
        return w[:-1]
