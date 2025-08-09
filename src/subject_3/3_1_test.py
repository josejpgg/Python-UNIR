
# Crear un programa que utilice un bucle while para sumar números
# hasta alcanzar un valor objetivo


# Escribe un programa que sume números enteros positivos ingresados
# por el usuario hasta alcanzar o superar un valor objetivo de 100. El programa debe:

# Inicializar una variable suma en 0 para llevar el registro de la suma acumulada
# Utilizar un bucle while que se ejecute mientras la suma sea menor que 100
# Dentro del bucle, solicitar al usuario que ingrese un número entero positivo
# Si el usuario ingresa un valor no numérico o un número negativo,
# mostrar un mensaje de error y continuar solicitando un nuevo número
# sin añadirlo a la suma
# Si el número es válido, añadirlo a la suma acumulada y mostrar el
# valor actual de la suma
# Cuando la suma alcance o supere 100, mostrar un mensaje indicando
# el valor final de la suma y cuántos números válidos fueron ingresados
# Puedes comenzar con este esquema:
    
# suma = 0
# contador = 0

# while suma < 100:
#     # Tu código aquí

# # Mensaje final

def sum_posivitve_numbers():
    sum = 0
    count = 0
    while sum < 100:
        try:
            number = int(input("Ingrese un número entero positivo: "))
            if number < 0:
                print("ERROR: El número debe ser positivo.")
                continue
            sum += number
            count += 1
            print(f"Suma actual: {sum}")
        except ValueError:
            print("ERROR: Entrada no válida. Por favor, ingrese un número entero positivo.")
    print(f"Suma final: {sum}. Se ingresaron {count} números válidos.")

sum_posivitve_numbers()

