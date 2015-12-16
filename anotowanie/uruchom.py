# coding=utf-8
from program import wczytaj_baze, wczytaj_wyniki
import pickle
from math import fabs
import operator

from program.Seq import Seq

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
# print bialka


prog = 20
wyniki = wczytaj_wyniki('data/cos.mgf')

for wynik in wyniki:
    # print 'Szukam sekwencji dla peptydu o ID:', wynik.ID
    for bialko in bialka:
        for peptyd in bialko.peptydy:
            if fabs(peptyd.masa - ((wynik.masa + Seq.atomy()['PROTON']) - wynik.ladunek + 1)) < (
                        wynik.masa / 10 ** 6) * prog:
                wynik.potencjalne[peptyd] = 0
    # print 'Znaleziono ', len(wynik.potencjalne), 'potencjalnie pasujących peptydów'
    if len(wynik.potencjalne) > 0:
        for fragment in wynik.fragmenty:
            for peptyd in wynik.potencjalne.keys():
                for jony in peptyd.jony:
                    if fabs(jony.b.masa - fragment) < (fragment / 10 ** 6) * prog:
                        wynik.potencjalne[peptyd] += 1
                        print "B"
                    if fabs(jony.y.masa - fragment) < (fragment / 10 ** 6) * prog:
                        wynik.potencjalne[peptyd] += 1
                        print "Y"
        najlepszy = max(wynik.potencjalne.iteritems(), key=operator.itemgetter(1))[0]
        if wynik.potencjalne[najlepszy] >= 0.05 * len(wynik.fragmenty):
            wynik.najlepszy = najlepszy
            print 'najlepszy fragment to:', wynik.najlepszy.seq
    else:
        # print 'Brak fragmentu spełniającego kryteria'
        pass

print 'Skończono dopasowywać peptydy!'

pickle.dump(wyniki, open('wyniki', 'wb'))

# wyniki = pickle.load(open('wyniki'))

with open('data/wyniki_anotowane_' + str(prog) + '.txt', 'w') as plik:
    for wynik in wyniki:
        plik.write(str(wynik))
