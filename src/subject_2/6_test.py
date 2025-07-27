from collections import Counter
import re

def analizar_texto(cadena_text):
    """
    Analiza una cadena de texta y devuelve un diccionario con estadisticas.
    Args:
        cadena_text
    Returns:
        diccionario con estadisticas.
    """
    total_caracteres = len(cadena_text)
    caracteres_sin_espacio = [caracter for caracter in cadena_text if caracter.strip()]
    frecuencia = Counter(caracteres_sin_espacio)
    total_sin_espacios = sum(len(caracter) for caracter in cadena_text if caracter.strip())
    return {
        "caracteres_mas_comunes" : frecuencia.most_common(3),
        "total_caracteres" : total_caracteres,
        "total_sin_espacios": total_sin_espacios
    }

resultado = analizar_texto("Hola, mundo! Este es un ejemplo.")
print(resultado)