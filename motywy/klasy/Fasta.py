# coding=utf-8


class Fasta(object):
    def __init__(self, header, seq):
        self.header = header
        self.seq = seq

    def __str__(self):
        return 'Fasta(' + self.header + ', ' + self.seq + ')'

    def __repr__(self):
        return 'Fasta(' + self.header + ', ' + self.seq + ')'
