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


    def __int__(self):
        return self.liczba_arabska

    def __str__(self):
        return f"{self.arabska_na_rzymska()} ({self.liczba_arabska})"

    def __eq__(self, other):
        return self.liczba_arabska == other.liczba_arabska

    def __le__(self, other):
        return self.liczba_arabska <= other.liczba_arabska

    def __gt__(self, other):
        return self.liczba_arabska > other.liczba_arabska

    def __add__(self, other):
        return LiczbaRzymska(self.liczba_arabska + other.liczba_arabska)

    def __iadd__(self, other):
        self.liczba_arabska += other.liczba_arabska
        return self

    def __contains__(self, litera):
        return litera in self.arabska_na_rzymska()

    def __len__(self):
        return len(self.arabska_na_rzymska())

    def __mul__(self, other):
        return LiczbaRzymska(self.liczba_arabska * other.liczba_arabska)

    def __sub__(self, other):
        return LiczbaRzymska(self.liczba_arabska - other.liczba_arabska)