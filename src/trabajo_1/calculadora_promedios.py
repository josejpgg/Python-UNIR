# Implementa una función llamada ingresar_calificaciones() que permita al usuario introducir el nombre de una materia y su calificación correspondiente. Esta función debe:

def ingresar_calificaciones() -> list:
    # Solicitar al usuario que ingrese el nombre de la materia
    # Solicitar la calificación (validando que sea un número entre 0 y 10)
    # Almacenar ambos datos en dos listas separadas (una para nombres y otra para calificaciones)
    # Preguntar si desea continuar ingresando más materias
    # Retornar ambas listas cuando el usuario decida terminar
    materia = []
    calificacion = []
    while True:
        materia.append(input("Ingrese el nombre de la materia: "))
        while True:
            cal_valor = input("Ingresa la calificación (0-10): ")
            # check if cal_valor is a number
            if cal_valor.isnumeric():
                cal_valor = float(cal_valor)
                if not 0.0 <= cal_valor <= 10.0:
                    print("Calificación invalida. Debe estar entre 0 y 10.")
                else:
                    calificacion.append(cal_valor)
                    break
            else:
                print("Calificación invalida. Debe estar entre 0 y 10.")
        if input("¿Desea ingresar otra materia? (s/n): ").lower() != 's':
            break
    return materia, calificacion

# Crea una función calcular_promedio(calificaciones) que reciba una lista de calificaciones y devuelva el promedio de todas ellas.
def calcular_promedio(calificaciones:list) -> float:
    return sum(calificaciones) / len(calificaciones) if calificaciones else 0

# Desarrolla una función determinar_estado(calificaciones, umbral) que reciba la lista de calificaciones y un valor umbral (por defecto 5.0), y devuelva dos listas: una con los índices de las materias aprobadas y otra con los índices de las reprobadas.
def determinar_estado(calificaciones:list, umbral:float=5.0) -> list:
    aprobadas = []
    reprobadas = []
    for index, calificacion in enumerate(calificaciones):
        if calificacion >= umbral:
            aprobadas.append(index)
        else:
            reprobadas.append(index)
    return aprobadas, reprobadas

# Implementa una función encontrar_extremos(calificaciones) que identifique el índice de la calificación más alta y el índice de la más baja en la lista de calificaciones.
def encontrar_extremos(calificaciones:list) -> int:
    if not calificaciones:
        return None, None
    max_val = max(calificaciones)
    min_val = min(calificaciones)
    max_index = []
    min_index = []
    if max_val != min_val:
        min_index = [index for index, calificacion in enumerate(calificaciones) if calificacion == min_val]
    max_index = [index for index, calificacion in enumerate(calificaciones) if calificacion == max_val]
    return max_index, min_index

# Todas las materias con sus calificaciones
# El promedio general
# Las materias aprobadas y reprobadas
# La materia con mejor calificación y su valor
# La materia con peor calificación y su valor
# Asegúrate de manejar casos especiales, como cuando no se ingresa ninguna materia, utilizando estructuras condicionales apropiadas.
if __name__ == "__main__":
    materias, calificaciones = ingresar_calificaciones()
    if len(materias) != len(calificaciones):
        raise ValueError("Cantidad de materias y calificaciones no coincide.")
    if materias == [] or calificaciones == []:
        raise ValueError("No se ingresaron materias o calificaciones.")
    print("\nMATERIAS Y CALIFICACIONES")
    for index, materia in enumerate(materias):
        print(f"Materia: {materia} \t Calificación: {calificaciones[index]}")
    print(f"PROMEDIO GENERAL: {calcular_promedio(calificaciones)}")
    aprobadas, reprobadas = determinar_estado(calificaciones)
    if len(aprobadas) == 0:
        print("No hay materias aprobadas.")
    else:
        print("\nMATERIAS APROBADAS")
        for index in aprobadas:
            print(f"Materia: {materias[index]} \t Calificación: {calificaciones[index]}")
    if len(reprobadas) == 0:
        print("No hay materias reprobadas.")
    else:
        print("\nMATERIAS REPROBADAS")
        for index in reprobadas:
            print(f"Materia: {materias[index]} \t CALIFICACIÓN {calificaciones[index]}")
    max_index, min_index = encontrar_extremos(calificaciones)
    print("\nMATERIA CON MAYOR CALIFICACIÓN")
    for index in max_index:
        print(f"Materia: {materias[index]} \t Calificación: {calificaciones[index]}")
    print("\nMATERIA CON MENOR CALIFICACIÓN")
    for index in min_index:
        print(f"Materia: {materias[index]} \t Calificación: {calificaciones[index]}")
