import pytest

from liczba_rzymska import LiczbaRzymska

def test_initialization():
    number = LiczbaRzymska(150)
    assert number.liczba_arabska == 150

def test_str_method():
    number = LiczbaRzymska(150)
    assert number.arabska_na_rzymska() == "CL"


