
usuario = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

# Iterando sobre las claves
for clave in usuario:
    print(f"Clave: {clave}, Valor: {usuario[clave]}")

# Iterando sobre los valores
for valor in usuario.values():
    print(f"Valor: {valor}")

# Iterando sobre pares clave-valor
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")









# Si las secuencias tienen longitudes diferentes, zip() se detiene cuando se
# agota la secuencia más corta. Para iterar hasta la secuencia más larga
# (rellenando con None los valores faltantes), puedes usar itertools.zip_longest():


from itertools import zip_longest

a = [1, 2]
b = [10, 20, 30, 40]

for x, y in zip_longest(a, b):
    print(f"x: {x}, y: {y}")




# Implementación de algoritmos de búsqueda

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if lista[medio] == objetivo:
            return medio  # Encontrado
        elif lista[medio] < objetivo:
            izquierda = medio + 1  # Buscar en la mitad derecha
        else:
            derecha = medio - 1  # Buscar en la mitad izquierda
            
    return -1  # No encontrado

# Ejemplo de uso
numeros = [1, 3, 5, 7, 9, 11, 13, 15]
indice = busqueda_binaria(numeros, 7)
print(f"El número 7 está en el índice: {indice}")




