# Crear un programa que determine la categoría de edad de una persona


# Crea un programa que solicite la edad de una persona y determine
# su categoría según las siguientes reglas:

# Si la edad es menor que 0, mostrar "Edad no válida"
# Si la edad está entre 0 y 12, mostrar "Infante"
# Si la edad está entre 13 y 17, mostrar "Adolescente"
# Si la edad está entre 18 y 64, mostrar "Adulto"
# Si la edad es 65 o mayor, mostrar "Adulto mayor"
# Utiliza una estructura if-elif-else para implementar esta lógica.
# El programa debe solicitar la edad con la función input() y convertirla
#a entero antes de evaluarla.

edad = int(input("Introduce tu edad: "))

if edad < 0:
    print("Edad no válida")
elif 0 <= edad <= 12:
    print("Infante")
elif 13 <= edad <= 17:
    print("Adolescente")
elif 18 <= edad <= 64:
    print("Adulto")
elif edad >= 65:
    print("Adulto mayor")
