
# Crea una calculadora básica que utilice operadores aritméticos
# para realizar operaciones matemáticas.


# Crea una calculadora básica que realice las cuatro operaciones
# aritméticas fundamentales (suma, resta, multiplicación y división) entre dos números.

# Debes solicitar al usuario que introduzca dos números y luego
# mostrar el resultado de las cuatro operaciones con estos números.

# Para cada operación, muestra el resultado con el siguiente formato:

# "La suma de X y Y es: Z"
# "La resta de X y Y es: Z"
# "La multiplicación de X y Y es: Z"
# "La división de X y Y es: Z"
# Recuerda manejar el caso especial de división por cero mostrando
# un mensaje apropiado.

# Pista: Utiliza los operadores +, -, *, / y controla la división
# por cero con una estructura condicional.

x = float(input("Introduce el primer número: "))
y = float(input("Introduce el segundo número: "))


print(f"La suma de X y Y es: {x + y}")
print(f"La resta de X y Y es: {x - y}")
print(f"La multiplicación de X y Y es: {x * y}")
print(f"La división de X y Y es: {x / y if y != 0 else 'No se puede dividir por cero'}")
