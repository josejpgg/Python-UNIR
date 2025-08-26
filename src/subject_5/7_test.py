# Crea un módulo llamado operaciones_matematicas.py que contenga las siguientes funciones:

# sumar(a, b): Devuelve la suma de dos números
# restar(a, b): Devuelve la resta de dos números
# multiplicar(a, b): Devuelve el producto de dos números
# dividir(a, b): Devuelve la división de a entre b (debe manejar la división por cero devolviendo un mensaje de error)
# Además, define una constante PI con el valor 3.14159.

# Luego, crea un archivo principal llamado calculadora.py que importe el módulo que has creado y realice las siguientes operaciones:

# Importa todas las funciones y la constante PI del módulo
# Calcula y muestra el resultado de sumar 15 y 7
# Calcula y muestra el resultado de multiplicar 3.5 por 2
# Calcula y muestra el área de un círculo con radio 5 utilizando la constante PI
# Puedes empezar creando primero el archivo operaciones_matematicas.py con las funciones solicitadas, y luego el archivo calculadora.py que importa y usa esas funciones.


# operaciones_matematicas.py
def sumar(a, b):
	return a + b

def restar(a, b):
	return a - b

def multiplicar(a, b):
	return a * b

def dividir(a, b):
	if b == 0:
		raise ValueError("No se puede dividir por cero.")
	return a / b

PI = 3.14159

# calculadora.py
from operaciones_matematicas import sumar, restar, multiplicar, dividir, PI

print("Suma de 15 y 7:", sumar(15, 7))
print("Multiplicación de 3.5 y 2:", multiplicar(3.5, 2))
radio = 5
area_circulo = PI * multiplicar(radio, radio)
print("Área de un círculo con radio 5:", area_circulo)
