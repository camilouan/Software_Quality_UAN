import requests
import time

def analizar_texto(url):
    for intento in range(3):
        try:
            resp = requests.get(url, timeout=5)
            resp.raise_for_status()
            texto = resp.text
            lineas = texto.split('\n')
            num_caracteres = sum(len(l) for l in lineas)
            return len(lineas), num_caracteres
        except requests.RequestException:
            if intento == 2:
                raise RuntimeError("No se pudo acceder a la URL después de 3 intentos")
            time.sleep(0.1)