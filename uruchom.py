# coding=utf-8
from program import wczytaj

i = 'data/small_20140127.fasta'
o = i.split('.')[0] + '_wyniki.txt'
p = open(o, 'w')
bialka = wczytaj(i)
for bialko in bialka:
    p.write(str(bialko))
p.close()
