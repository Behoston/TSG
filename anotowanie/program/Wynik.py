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
