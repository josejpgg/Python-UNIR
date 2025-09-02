# Dada una lista de números enteros, crea una función llamada procesar_numeros que realice las siguientes operaciones:

# Filtra solo los números pares de la lista usando la función filter()
# Aplica una transformación a cada número par para duplicar su valor usando la función map()
# Devuelve una lista con los resultados
# Por ejemplo, si la entrada es [1, 2, 3, 4, 5, 6], la salida debe ser [4, 8, 12] (los números pares 2, 4 y 6 filtrados y luego duplicados).


numeros = [1, 2, 3, 4, 5, 6]

def procesar_numeros(lista: list):
	numeros_pares = filter(lambda x: x % 2 == 0, lista)
	numeros_duplicados = map(lambda x: x * 2, numeros_pares)
	return list(numeros_duplicados)

print(procesar_numeros(numeros))
