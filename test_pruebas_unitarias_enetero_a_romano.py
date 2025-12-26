from main import entero_a_romano,RomanNumberError


def test_entero_romano_1994():
    assert entero_a_romano(1994) == 'MCMXCIV'

def test_entero_romano_3():
    assert entero_a_romano(3) == "III"

def test_entero_romano_33():
    assert entero_a_romano(33) == "XXXIII"    

def test_entero_romano_333():
    assert entero_a_romano(333) == "CCCXXXIII"

def test_valor_maximo_3999():
    with pytest.raises(RomanNumberError) as exeptionInfo:
        entero_a_romano(4000)
    assert str(exeptionInfo.value) == "El limite esta entre mayor a 0 y 3999"

def test_valor_cero():
    assert entero_a_romano(0) == ""