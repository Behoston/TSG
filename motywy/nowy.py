# coding=utf-8
from random import randint

l = 10
iteracji = 10


def wczytaj_faste(plik):
    seqs = []
    with open(plik) as otwarty:
        for line in otwarty:
            if line[0] == '>':
                seqs.append('')
            else:
                for i in line.split():
                    seqs[-1] += i.strip()
    if len(seqs) > 0:
        dl = len(seqs[0])
        for i in xrange(len(seqs)):
            if dl != len(seqs[i]):
                print 'Sekwnecja o złej długości', seqs.pop(i)
    return seqs


def init(fasty):
    dlugosc = len(fasty[0])
    L = []
    LL = []
    for fasta in fasty:
        poczatek = randint(0, dlugosc - l)
        koniec = poczatek + l
        L.append(fasta[poczatek:koniec])
        LL.append(fasta[:poczatek] + fasta[koniec:])
    return L, LL


def licz_teta(macierz_L):
    teta = []
    for motyw in macierz_L:
        teta.append({'A': 0, 'C': 0, 'T': 0, 'G': 0})
        for litera in motyw:
            teta[-1][litera] += 1
    ilosc_sekwencji_w_L = float(len(macierz_L))
    for wiersz in xrange(len(teta)):
        for klucz in teta[wiersz].keys():
            teta[wiersz][klucz] /= ilosc_sekwencji_w_L
    return teta


def licz_teta_zero(macierz_LL):
    teta_zero = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
    ilosc = 0
    for wiersz in macierz_LL:
        for litera in wiersz:
            teta_zero[litera] += 1
            ilosc += 1
    ilosc = float(ilosc)
    teta_zero['A'] /= ilosc
    teta_zero['C'] /= ilosc
    teta_zero['T'] /= ilosc
    teta_zero['G'] /= ilosc
    return teta_zero


def losuj(fasty, l):
    idx_wylosowana = randint(len(fasty) - 1)
    wylosowana = fasty[idx_wylosowana]
    L = []
    for poczatek in xrange(len(wylosowana) - l):
        koniec = poczatek + l
        L.append(wylosowana[poczatek:koniec])


def licz_prawdopodobienstwo(teta, teta_zero, seq):
    x = 1.0
    y = 1.0
    for i in xrange(len(seq)):
        y *= teta_zero[seq[i]]
        x *= teta[i][seq[i]]
    return x / y


fasty = wczytaj_faste('data/pho.fasta')
L, LL = init(fasty)
teta = licz_teta(L)
tea_zero = licz_teta_zero(LL)
