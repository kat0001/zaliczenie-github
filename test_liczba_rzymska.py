import pytest

from liczba_rzymska import LiczbaRzymska

@pytest.mark.parametrize("invalid_input", ["abc", None, [], {}, "", "12.5"])
def test_invalid_inputs_raise_error(invalid_input):
    with pytest.raises((ValueError, TypeError)):
        LiczbaRzymska(invalid_input)

def test_initialization():
    number = LiczbaRzymska(150)
    assert number.liczba_arabska == 150

def test_str_method():
    number = LiczbaRzymska(150)
    assert number.arabska_na_rzymska() == "CL"

def test_int_method():
    liczba = LiczbaRzymska("200")
    assert int(liczba) == 200

def test_equality_and_comparison():
    a = LiczbaRzymska(100)
    b = LiczbaRzymska(100)
    c = LiczbaRzymska(200)
    assert a == b
    assert a < c
    assert c > b

def test_addition():
    a = LiczbaRzymska(150)
    b = LiczbaRzymska(2395)
    result = a + b
    assert isinstance(result, LiczbaRzymska)
    assert int(result) == 2545
    assert str(result) == "MMDXLV (2545)"

def test_in_place_addition():
    a = LiczbaRzymska(150)
    b = LiczbaRzymska(2395)
    a += b
    assert int(a) == 2545
    assert str(a) == "MMDXLV (2545)"

def test_contains():
    a = LiczbaRzymska(150)
    assert "L" in a
    assert "X" not in a
    assert "V" not in a

def test_length():
    a = LiczbaRzymska(150)
    assert len(a) == 2  # "CL"

def test_multiplication():
    c = LiczbaRzymska(3)
    d = LiczbaRzymska(8)
    result = c * d
    assert isinstance(result, LiczbaRzymska)
    assert int(result) == 24
    assert str(result) == "XXIV (24)"

def test_subtraction():
    d = LiczbaRzymska(8)
    c = LiczbaRzymska(3)
    result = d - c
    assert int(result) == 5
    assert str(result) == "V (5)"

def test_subtraction_negative_result():
    c = LiczbaRzymska(3)
    d = LiczbaRzymska(8)
    with pytest.raises(ValueError):
        _ = c - d


