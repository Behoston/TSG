from collections import defaultdict


class Seq(object):
    @staticmethod
    def aminokwasy():
        aminokwasy = defaultdict(dict)
        A = {'C': 3, 'H': 5, 'N': 1, 'O': 1}
        aminokwasy['A'] = A
        C = {'C': 3, 'H': 5, 'N': 1, 'O': 1, 'S': 1}
        aminokwasy['C'] = C
        D = {'C': 4, 'H': 5, 'N': 1, 'O': 3}
        aminokwasy['D'] = D
        E = {'C': 5, 'H': 7, 'N': 1, 'O': 3}
        aminokwasy['E'] = E
        F = {'C': 9, 'H': 9, 'N': 1, 'O': 1}
        aminokwasy['F'] = F
        G = {'C': 2, 'H': 3, 'N': 1, 'O': 1}
        aminokwasy['G'] = G
        H = {'C': 6, 'H': 7, 'N': 3, 'O': 1}
        aminokwasy['H'] = H
        I = {'C': 6, 'H': 11, 'N': 1, 'O': 1}
        aminokwasy['I'] = I
        K = {'C': 6, 'H': 12, 'N': 2, 'O': 1}
        aminokwasy['K'] = K
        L = {'C': 6, 'H': 11, 'N': 1, 'O': 1}
        aminokwasy['L'] = L
        M = {'C': 5, 'H': 9, 'N': 1, 'O': 1, 'S': 1}
        aminokwasy['M'] = M
        N = {'C': 4, 'H': 6, 'N': 2, 'O': 2}
        aminokwasy['N'] = N
        P = {'C': 5, 'H': 7, 'N': 1, 'O': 1}
        aminokwasy['P'] = P
        Q = {'C': 5, 'H': 8, 'N': 2, 'O': 2}
        aminokwasy['Q'] = Q
        R = {'C': 6, 'H': 12, 'N': 4, 'O': 1}
        aminokwasy['R'] = R
        S = {'C': 3, 'H': 5, 'N': 1, 'O': 2}
        aminokwasy['S'] = S
        T = {'C': 4, 'H': 7, 'N': 1, 'O': 2}
        aminokwasy['T'] = T
        V = {'C': 5, 'H': 9, 'N': 1, 'O': 1}
        aminokwasy['V'] = V
        W = {'C': 11, 'H': 10, 'N': 2, 'O': 1}
        aminokwasy['W'] = W
        Y = {'C': 9, 'H': 9, 'N': 1, 'O': 2}
        aminokwasy['Y'] = Y

        return aminokwasy

    @staticmethod
    def atomy():
        return {'C': 12, 'H': 1.0078250320710, 'O': 15.9949146195616, 'S': 31.9720710015, 'N': 14.00307400486,
                'PROTON': 1.00727646681290}

    def policz_mase(self, seq):
        masa = 0.0
        for aminokwas in seq:
            for atom in self.aminokwasy()[aminokwas].items():
                masa += atom[1] * self.atomy()[atom[0]]
        return masa

    def __init__(self, seq):
        self.seq = seq
        self.masa = self.policz_mase(self.seq)

    def __str__(self):
        return self.seq

    def __repr__(self):
        return type(self).__name__ + '(' + self.seq + ')'
