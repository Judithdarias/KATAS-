from main import romano_a_entero,RomanNumberError
import pytest

def test_romano_a_entero_I():
    assert romano_a_entero("I")==1

def test_romano_a_entero_MDCCXIII():
    assert romano_a_entero('MDCCXIII') == 1713

def test_romano_a_entero_IV():
    assert romano_a_entero("IV")==4

def test_romano_a_entero_no_repetir_3_veces01():
    with pytest.raises( RomanNumberError ) as exeptionInfo:
        romano_a_entero("IIII")
    assert str(exeptionInfo.value) == "No se puede repetir el valor mas de tres veces"

def test_romano_a_entero_no_repetir_3_veces02():
    with pytest.raises( RomanNumberError ) as exeptionInfo:
        romano_a_entero("XXXX")
    assert str(exeptionInfo.value) == "No se puede repetir el valor mas de tres veces"  


def test_romano_a_entero_no_repetir_3_veces03():
    with pytest.raises( RomanNumberError ) as exeptionInfo:
        romano_a_entero("CCCC")
    assert str(exeptionInfo.value) == "No se puede repetir el valor mas de tres veces"  

def test_romano_a_entero_no_repetir_3_veces04():
    with pytest.raises( RomanNumberError ) as exeptionInfo:
        romano_a_entero("MMMM")
    assert str(exeptionInfo.value) == "No se puede repetir el valor mas de tres veces" 

def test_romano_a_entero_no_repetir_01():
    with pytest.raises( RomanNumberError ) as exeptionInfo:
        romano_a_entero("DD")
    assert str(exeptionInfo.value) == "Los caracteres 'D' 'L' y 'V' no se pueden repetir" 

def test_romano_a_entero_no_repetir_02():
    with pytest.raises( RomanNumberError ) as exeptionInfo:
        romano_a_entero("LL")
    assert str(exeptionInfo.value) == "Los caracteres 'D' 'L' y 'V' no se pueden repetir" 

def test_romano_a_entero_no_repetir_03():
    with pytest.raises( RomanNumberError ) as exeptionInfo:
        romano_a_entero("VV")
    assert str(exeptionInfo.value) == "Los caracteres 'D' 'L' y 'V' no se pueden repetir" 


def test_romano_solo_se_resta01():
    with pytest.raises( RomanNumberError ) as exeptionInfo:
        romano_a_entero("IL")
    assert str(exeptionInfo.value) == 'I solo se puede restar de V y X'

def test_romano_solo_se_resta02():
    with pytest.raises( RomanNumberError ) as exeptionInfo:
        romano_a_entero("XM")
    assert str(exeptionInfo.value) == 'X solo se puede restar de L y C' 
"""
def test_romano_solo_se_resta03():
    with pytest.raises( RomanNumberError ) as exeptionInfo:
        romano_a_entero("XM")
    assert str(exeptionInfo.value) == 'C solo se puede restar de D y M' 
"""