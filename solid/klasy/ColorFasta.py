# coding=utf-8


class ColorFasta:
    @staticmethod
    def decode_one(amino, number):
        if amino == 'A':
            if number == 0:
                return 'A'
            elif number == 1:
                return 'C'
            elif number == 2:
                return 'G'
            else:
                return 'T'
        elif amino == 'C':
            if number == 0:
                return 'C'
            elif number == 1:
                return 'A'
            elif number == 2:
                return 'T'
            else:
                return 'G'
        elif amino == 'G':
            if number == 0:
                return 'G'
            elif number == 1:
                return 'T'
            elif number == 2:
                return 'A'
            else:
                return 'C'
        else:  # amino == 'T'
            if number == 0:
                return 'T'
            elif number == 1:
                return 'G'
            elif number == 2:
                return 'C'
            else:
                return 'A'

    def decode(self):
        for number in self.color_seq[1:]:
            self.seq += self.decode_one(self.seq[-1], int(number))

    def __init__(self, header, color_seq):
        self.color_seq = color_seq
        self.header = header
        self.seq = self.color_seq[0]
        self.decode()
