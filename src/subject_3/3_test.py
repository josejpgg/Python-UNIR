
# Crear una función que sume los números pares en un rango dado

# Crea una función llamada suma_pares que reciba dos parámetros: inicio y fin.
# La función debe calcular y devolver la suma de todos los números pares que se
# encuentran en el rango desde inicio hasta fin (ambos inclusive).

# Por ejemplo:

# Si llamamos suma_pares(1, 10) debe devolver 30 (2+4+6+8+10)
# Si llamamos suma_pares(5, 15) debe devolver 50 (6+8+10+12+14)
# Utiliza un bucle for con la función range() para iterar sobre el
# rango de números y suma solo aquellos que sean pares
# (pista: puedes usar el operador módulo % para verificar si un número es par).

def suma_pares(inicio:int, fin:int) -> int:
    sum_pair = 0
    for number in range(inicio, fin + 1):
        if number % 2 == 0:
            sum_pair += number
    return sum_pair

print(suma_pares(1, 10))
print(suma_pares(5, 15))
