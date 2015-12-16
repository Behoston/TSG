# coding=utf-8
""" Program do składania sekwencji z spektrometrii mas """
from copy import copy

from program.Bialko import Bialko
from program.Wynik import Wynik

__version__ = "0.2"
__author__ = "Behoston"
__author_email__ = "mlegiecki@gmail.com"


def wczytaj_baze(plik):
    seqs = []
    with open(plik) as otwarty:
        for line in otwarty:
            if line[0] == '>':
                seqs.append([line, ''])
            else:
                for i in line.split():
                    seqs[-1][1] += i.strip()
    bialka = []
    for seq in seqs:
        bialka.append(Bialko(seq[1], seq[0]))
    return bialka


def wczytaj_wyniki(plik):
    wyniki = []
    with open(plik) as otwarty:
        zaczety_jon = False
        ID = 0
        ladunek = 0
        stosunek = 0
        fragmenty = []
        for line in otwarty:
            if line[:10] == 'BEGIN IONS':
                zaczety_jon = True
            elif line[:6] == 'CHARGE':
                ladunek = int(line.split('=')[1].strip()[:-1])
            elif line[:7] == 'PEPMASS':
                stosunek = float(line.split('=')[1].split()[0])
            elif line[:5] == 'TITLE':
                ID = int(line.split('=')[1].split(':')[0])
            elif zaczety_jon and line[0].isdigit():
                fragmenty.append(float(line.split()[0]))
            elif line[:8] == 'END IONS':
                wyniki.append(Wynik(ID, stosunek, ladunek, copy(fragmenty)))
                zaczety_jon = False
                fragmenty = []
    return wyniki
