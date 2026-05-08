from unittest.mock import Mock, patch, call
import pytest
from requests.exceptions import RequestException, Timeout
from src.analizador import analizar_texto


class TestAnalizarTextoConMocks:
    """Tests para analizar_texto usando mocks de requests."""
    
    @patch('src.analizador.requests.get')
    def test_analizar_texto_exitoso(self, mock_get):
        """Simula respuesta HTTP exitosa."""
        # Preparar el mock
        mock_response = Mock()
        mock_response.text = "línea 1\nlínea 2\nlínea 3"
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        # Ejecutar
        lineas, caracteres = analizar_texto("http://ejemplo.com/archivo.txt")
        
        # Verificar
        assert lineas == 3
        assert caracteres == 21  # "línea 1\nlínea 2\nlínea 3" sin contar \n
        mock_get.assert_called_once_with("http://ejemplo.com/archivo.txt", timeout=5)
    
    @patch('src.analizador.requests.get')
    def test_analizar_texto_fallo_con_reintento(self, mock_get):
        """Simula fallo en primer intento y éxito en el segundo."""
        # Configurar: Fallo en intento 1, éxito en intento 2
        mock_response_exitosa = Mock()
        mock_response_exitosa.text = "línea única"
        mock_response_exitosa.raise_for_status.return_value = None
        
        mock_get.side_effect = [
            RequestException("Connection error"),  # Intento 1 falla
            mock_response_exitosa                  # Intento 2 exitoso
        ]
        
        # Ejecutar
        lineas, caracteres = analizar_texto("http://ejemplo.com/archivo.txt")
        
        # Verificar
        assert lineas == 1
        assert caracteres == 11
        assert mock_get.call_count == 2  # Se llamó dos veces
    
    @patch('src.analizador.requests.get')
    def test_analizar_texto_fallo_total(self, mock_get):
        """Simula fallo en los 3 intentos."""
        # Todos los intentos fallan
        mock_get.side_effect = RequestException("Connection error")
        
        # Ejecutar y verificar que lanza RuntimeError
        with pytest.raises(RuntimeError) as excinfo:
            analizar_texto("http://ejemplo.com/archivo.txt")
        
        assert "No se pudo acceder" in str(excinfo.value)
        assert mock_get.call_count == 3  # Se llamó 3 veces
    
    @patch('src.analizador.requests.get')
    def test_analizar_texto_respuesta_vacía(self, mock_get):
        """Simula respuesta HTTP con contenido vacío."""
        mock_response = Mock()
        mock_response.text = ""
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        lineas, caracteres = analizar_texto("http://ejemplo.com/vacio.txt")
        
        # Una línea vacía = 1 línea, 0 caracteres
        assert lineas == 1
        assert caracteres == 0
    
    @patch('src.analizador.requests.get')
    def test_timeout_con_reintento(self, mock_get):
        """Simula timeout que se recupera en reintento."""
        mock_response_exitosa = Mock()
        mock_response_exitosa.text = "recuperado"
        mock_response_exitosa.raise_for_status.return_value = None
        
        mock_get.side_effect = [
            Timeout("Timeout"),      # Intento 1: Timeout
            mock_response_exitosa    # Intento 2: Éxito
        ]
        
        lineas, caracteres = analizar_texto("http://ejemplo.com/archivo.txt")
        
        assert lineas == 1
        assert caracteres == 10

