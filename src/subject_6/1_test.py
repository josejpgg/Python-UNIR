# Crea un programa que solicite al usuario introducir un número entero por consola. El programa debe manejar posibles errores utilizando un bloque try-except:

# Si el usuario introduce algo que no es un número entero, debe capturar la excepción ValueError y mostrar el mensaje: "Error: Debes introducir un número entero."

# Si el usuario interrumpe la ejecución (por ejemplo, con Ctrl+C), debe capturar la excepción KeyboardInterrupt y mostrar el mensaje: "Se ha interrumpido la ejecución del programa."

# Si la operación se completa correctamente, debe mostrar: "Has introducido el número: [número]".

# Para empezar, utiliza la función input() para solicitar la entrada y la función int() para convertirla a entero dentro del bloque try.


try:
	number = int(input("Introducir número entero: "))
	print(f"Has introducido el número: {number}")
except (ValueError):
	print("Error: Debes introducir un número entero.")
except (KeyboardInterrupt):
	print("Se ha interrumpido la ejecución del programa.")