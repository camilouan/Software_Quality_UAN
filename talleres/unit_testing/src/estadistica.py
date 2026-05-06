def calcular_promedio(numeros):
    if not numeros:
        return None
    return sum(numeros) / len(numeros)