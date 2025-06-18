class LiczbaRzymska:

    def __init__(self, liczba_arabska):
        self.liczba_arabska = int(liczba_arabska)

    def arabska_na_rzymska(self):
        jednosci = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        dziesiatki = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        setki = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        arab = str(self.liczba_arabska)
        arab = f"{arab:0>4}"
        return int(arab[-4]) * "M" + setki[int(arab[-3])] + dziesiatki[int(arab[-2])] + jednosci[int(arab[-1])]
