# coding=utf-8
from solid.klasy.ColorFasta import ColorFasta


def load_color_fasta_file(plik):
    lista = []
    header = ''
    color_seq = ''
    with open(plik) as otwarty:
        for line in otwarty:
            if line[0] == '>':
                if header != '':
                    lista.append(ColorFasta(header, color_seq))
                header = line.strip()
                color_seq = ''
            else:
                for i in line.split():
                    color_seq += i.strip()
    return lista


zdekodowane = load_color_fasta_file('resources/short.csfasta')
for seq in zdekodowane:
    print seq.seq
