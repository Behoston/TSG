# coding=utf-8
from Bio import motifs

from klasy.Fasta import Fasta
from math import log, e


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


fasty = wczytaj_faste('data/cap.fasta')
n = len(fasty)
dlugosc = len(fasty[0].seq)
F = {
    'A': [0.0 for x in xrange(dlugosc)],
    'C': [0.0 for x in xrange(dlugosc)],
    'T': [0.0 for x in xrange(dlugosc)],
    'G': [0.0 for x in xrange(dlugosc)]}

for i in xrange(dlugosc):
    for fasta in fasty:
        for key in F.keys():
            if fasta.seq[i] == key:
                F[key][i] += 1
for lista in F.values():
    for i in xrange(dlugosc):
        lista[i] /= n
H = [0.0 for x in xrange(dlugosc)]
print 'F'
for (key, value) in F.items():
    print key, ':', value
    for i in xrange(len(value)):
        if value[i] != 0:
            H[i] += value[i] * log(value[i], 2)
for i in xrange(len(H)):
    H[i] *= -1
print '\nH'
print H
en = 3 / (2 * n * log(2, e))
print 'R'
R = [2 - (h + en) for h in H]
print R

print '\nWYNIKI'
for (key, value) in F.items():
    print key, ':', [round(value[i] * R[i], 3) for i in xrange(len(value))]
