# coding=utf-8
from klasy.Fasta import Fasta
from random import randint
from time import time

start_time = time()

l = 10
iter = 10


def wczytaj_faste(plik):
    seqs = []
    with open(plik) as otwarty:
        for line in otwarty:
            if line[0] == '>':
                seqs.append([line.strip(), ''])
            else:
                for i in line.split():
                    seqs[-1][1] += i.strip()
    fasty = []
    for seq in seqs:
        fasty.append(Fasta(seq[0], seq[1]))
    return fasty


fasty = wczytaj_faste('data/pho.fasta')
ile_wszystkich = len(fasty)
L = []
LL = []
O = []
OO = {'A': 0.0, 'C': 0.0, 'T': 0.0, 'G': 0.0}

maxL = len(fasty[0].seq) - l

for fasta in fasty:
    poczatek = randint(0, maxL)
    koniec = poczatek + l
    L.append(fasta.seq[poczatek: koniec])
    LL.append(fasta.seq[:poczatek] + fasta.seq[koniec:])


# for i in xrange(l):
#     O.append({'A': 0, 'C': 0, 'T': 0, 'G': 0})
#     for j in L:
#         O[i][j[i]] += 1
# for i in xrange(maxL):
#     OO.append({'A': 0, 'C': 0, 'T': 0, 'G': 0})
#     for j in LL:
#         OO[i][j[i]] += 1


def liczO(macierz_L, macierz_teta):
    ile_wszystkich = len(macierz_L)
    for i in xrange(len(macierz_L[0])):
        macierz_teta.append({'A': 0.0, 'C': 0.0, 'T': 0.0, 'G': 0.0})
        for j in macierz_L:
            macierz_teta[i][j[i]] += 1
    for i in xrange(ile_wszystkich):
        for klucz in macierz_teta[i].keys():
            macierz_teta[i][klucz] /= ile_wszystkich


def liczOO(macierz_LL, macierz_teta_zero):
    ile_wszystkich = 0
    for i in macierz_LL:
        for j in i:
            macierz_teta_zero[j] += 1
            ile_wszystkich += 1
    for klucz in macierz_teta_zero.keys():
        macierz_teta_zero[klucz] /= ile_wszystkich


liczO(L, O)
liczOO(LL, OO)

for i in xrange(iter):
    wylosowana = randint(0, ile_wszystkich - 1)
    jedna = fasty[wylosowana].seq
    for poczatek in xrange(0, maxL):
        koniec = poczatek + l
        jednejL = []
        jednejLL = []
        jednejO = []
        jednejOO = {'A': 0.0, 'C': 0.0, 'T': 0.0, 'G': 0.0}
        for j in xrange(ile_wszystkich):
            if j != wylosowana:
                jednejL.append(jedna[poczatek:koniec])
                jednejLL.append(jedna[:poczatek] + jedna[:koniec])
        liczO(jednejL, jednejO)
        wagi_L = []
        for j in xrange(len(jednejL)):
            wagi_L.append(1.0)
            for litera_idx in xrange(len(jednejL[j])):
                litera = jednejL[j][litera_idx]
                wagi_L[j] *= jednejO[j][litera]
        print wagi_L
        liczOO(jednejLL, jednejOO)

print 'Execution time', time() - start_time
