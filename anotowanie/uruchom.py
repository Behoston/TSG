# coding=utf-8
from program import wczytaj_baze, wczytaj_wyniki
import pickle
from math import fabs
import operator

i = 'data/small_20140127.fasta'
o = i.split('.')[0] + '_wyniki.txt'
oo = i.split('.')[0] + '_wyniki.object'
# p = open(o, 'w')

# bialka = wczytaj_baze(i)
# pickle.dump(bialka, open(oo, 'wb'))
# for bialko in bialka:
#     p.write(str(bialko))
# p.close()

bialka = pickle.load(open(oo))
print bialka

wyniki = wczytaj_wyniki('data/cos.mgf')

prog = 20

for wynik in wyniki:
    print 'Szukam sekwencji dla peptydu o ID:', wynik.ID
    for bialko in bialka:
        for peptyd in bialko.peptydy:
            if fabs(peptyd.masa - (wynik.masa - wynik.ladunek + 1)) < (wynik.masa / 10 ** 6) * prog:
                wynik.potencjalne[peptyd] = 0
    print 'Znaleziono ', len(wynik.potencjalne), 'potencjalnie pasujących peptydów'
    if len(wynik.potencjalne) > 0:
        for fragment in wynik.fragmenty:
            for peptyd in wynik.potencjalne.keys():
                for jony in peptyd.jony:
                    if fabs(jony.b.masa - fragment) < (fragment / 10 ** 6) * prog:
                        wynik.potencjalne[peptyd] += 1
                    if fabs(jony.y.masa - fragment) < (fragment / 10 ** 6) * prog:
                        wynik.potencjalne[peptyd] += 1
        wynik.najlepszy = max(wynik.potencjalne.iteritems(), key=operator.itemgetter(1))[0]
        print 'najlepszy fragment to:', wynik.najlepszy.seq

print 'Skończono dopasowywać peptydy!'

for wynik in wyniki:
    naj_id = ''
    if wynik.najlepszy:
        naj_id = wynik.najlepszy.seq
    print wynik.ID, naj_id
