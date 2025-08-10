# Crear una función que calcule el área de un rectángulo


# Crea una función llamada calcular_area_rectangulo que reciba dos parámetros:
# base y altura. La función debe calcular y retornar el área del rectángulo (base × altura).

# Luego, llama a la función con los valores 5 y 3, y almacena el resultado en
# una variable llamada area. Finalmente, imprime el resultado con un mensaje descriptivo.

def calcular_area_rectangulo(base:int, altura:int) -> int:
    return base * altura

area = calcular_area_rectangulo(5, 3)
print(f"El área del rectángulo es: {area}")
