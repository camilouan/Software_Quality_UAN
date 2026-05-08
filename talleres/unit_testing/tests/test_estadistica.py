import pytest
from src.estadistica import calcular_promedio

# ============= TESTS ORIGINALES (DÉBILES) =============
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


# ============= TESTS MEJORADOS (ROBUSTOS) =============

class TestCalcularPromedioMejorado:
    """Tests rigurosos que validan VALORES, no solo tipos."""
    
    def test_promedio_valores_simples(self):
        """Valida cálculo correcto con valores simples."""
        assert calcular_promedio([2, 4, 6]) == 4.0
    
    def test_promedio_un_elemento(self):
        """Caso especial: un solo elemento."""
        assert calcular_promedio([5]) == 5.0
    
    def test_promedio_dos_elementos(self):
        """Caso simple: dos elementos."""
        assert calcular_promedio([1, 3]) == 2.0
    
    def test_promedio_valores_negativos(self):
        """Valida manejo de números negativos."""
        assert calcular_promedio([-10, 0, 10]) == 0.0
    
    def test_promedio_decimales(self):
        """Valida cálculo con decimales."""
        result = calcular_promedio([1.5, 2.5, 3.0])
        assert pytest.approx(result) == 2.333333333333
    
    def test_promedio_resultado_impar(self):
        """Valida resultado que no es entero exacto."""
        result = calcular_promedio([1, 2, 3])
        assert pytest.approx(result) == 2.0
    
    def test_lista_vacia_retorna_none(self):
        """Lista vacía debe retornar None."""
        assert calcular_promedio([]) is None
    
    def test_tipo_retorno_es_float_o_none(self):
        """Valida que el tipo sea float o None (no int ni str)."""
        resultado_lista = calcular_promedio([1, 2, 3])
        resultado_vacia = calcular_promedio([])
        
        assert isinstance(resultado_lista, float)
        assert resultado_vacia is None
