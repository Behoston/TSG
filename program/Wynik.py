# coding=utf-8


class Wynik(object):
    def __init__(self, ID, stosunek_masy, ladunek, fragmenty):
        self.ID = ID
        self.stosunek_masy = stosunek_masy
        self.ladunek = ladunek
        self.fragmenty = fragmenty
        self.masa = stosunek_masy * ladunek
        self.potencjalne = {}
        self.najlepszy = None

    def sortuj_potencjalne(self):
        return sorted(list(self.potencjalne.items()), key=lambda p: p[1])

    def __str__(self):
        s = 'ID: ' + str(self.ID) + '\n'
        s += '\tmasa: ' + str(self.masa) + '\n'
        s += '\tIlość fragmentów: ' + str(len(self.fragmenty)) + '\n'
        for fragment in self.fragmenty:
            s += '\t\t' + str(fragment) + '\n'
        s += '\tPotencjalne peptydy[' + str(len(self.potencjalne)) + ']:\n'
        for (p, i) in self.potencjalne.items():
            s += '\t\tPasowało fragmentów: ' + str(i) + '\n'
            for line in str(p).split('\n'):
                s += '\t\t\t' + line + '\n'
        if self.najlepszy:
            s += '\tSeq: ' + self.najlepszy.seq + '\n'
            s += '\tNależy do białka: ' + self.najlepszy.nazwa_bialka + '\n'
        return s
