# coding=utf-8
""" Program do składania sekwencji z spektrometrii mas """
from program.Bialko import Bialko

__version__ = "0.2"
__author__ = "Behoston"
__author_email__ = "mlegiecki@gmail.com"


def wczytaj(plik):
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
