import pytest
from src.estadistica import calcular_promedio

def test_tipo_retorno_float():
    res = calcular_promedio([1, 2, 3])
    assert isinstance(res, float)

def test_lista_vacia_retorna_none():
    assert calcular_promedio([]) is None

def test_no_lanza_excepcion():
    try:
        calcular_promedio([5])
    except Exception:
        pytest.fail("No debería lanzar excepción")