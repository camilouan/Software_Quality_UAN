import pytest
from src.ordenador import ordenar


class TestOrdenarMejorado:
    """Tests robustos para la función ordenar()."""
    
    def test_lista_vacia(self):
        """Lista vacía retorna lista vacía."""
        assert ordenar([]) == []
    
    def test_un_elemento(self):
        """Un solo elemento retorna lista con ese elemento."""
        assert ordenar([5]) == [5]
    
    def test_lista_ya_ordenada(self):
        """Lista ya ordenada se mantiene igual."""
        assert ordenar([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    def test_lista_desordenada(self):
        """Lista desordenada se ordena correctamente."""
        assert ordenar([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
    
    def test_orden_descendente(self):
        """Lista en orden descendente se reordena ascendente."""
        assert ordenar([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    
    def test_numeros_duplicados(self):
        """Maneja correctamente números duplicados."""
        assert ordenar([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]
    
    def test_numeros_negativos(self):
        """Ordena correctamente números negativos."""
        assert ordenar([3, -1, 0, -5, 2]) == [-5, -1, 0, 2, 3]
    
    def test_numeros_negativos_y_positivos(self):
        """Ordena mix de negativos, ceros y positivos."""
        assert ordenar([-3, 1, -1, 0, 2]) == [-3, -1, 0, 1, 2]
    
    def test_flotantes(self):
        """Ordena números decimales correctamente."""
        assert ordenar([3.5, 1.1, 2.9, 1.1]) == [1.1, 1.1, 2.9, 3.5]
    
    def test_orden_ascendente_verificado(self):
        """Verifica que el resultado está en orden ascendente."""
        result = ordenar([5, 2, 8, 1, 9, 3])
        # Verificar que cada elemento es <= al siguiente
        for i in range(len(result) - 1):
            assert result[i] <= result[i + 1], f"{result[i]} > {result[i+1]}"
    
    def test_cantidad_elementos_preservada(self):
        """La cantidad de elementos se preserva después de ordenar."""
        original = [5, 2, 8, 1, 9, 3, 7]
        resultado = ordenar(original)
        assert len(resultado) == len(original)
    
    def test_elementos_preservados(self):
        """Los mismos elementos están presentes después de ordenar."""
        original = [5, 2, 8, 1, 9, 3, 7]
        resultado = ordenar(original)
        assert sorted(original) == sorted(resultado)
        # Contar ocurrencias
        for elem in original:
            assert original.count(elem) == resultado.count(elem)
