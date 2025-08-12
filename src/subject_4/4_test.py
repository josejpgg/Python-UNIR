# Crea tres funciones lambda y asígnalas a variables con los siguientes nombres y comportamientos:

# cuadrado: una función que reciba un número y devuelva su cuadrado.
# es_par: una función que reciba un número y devuelva True si es par o False si es impar.
# suma: una función que reciba dos números y devuelva su suma.
# Luego, crea una lista llamada numeros con los valores [1, 2, 3, 4, 5] y utiliza la función map() con tu lambda cuadrado para crear una nueva lista llamada cuadrados que contenga el cuadrado de cada número.

# Finalmente, utiliza la función filter() con tu lambda es_par para crear una lista llamada pares que contenga solo los números pares de la lista original.

cuadrado = lambda x: x ** 2
es_par = lambda x: x % 2 == 0
suma = lambda x, y: x + y

valores = [1, 2, 3, 4, 5]
cuadrados = list(map(cuadrado, valores))
pares = list(filter(es_par, valores))

print(cuadrados)  # Imprime: [1, 4, 9, 16, 25]
print(pares)      # Imprime: [2, 4]
