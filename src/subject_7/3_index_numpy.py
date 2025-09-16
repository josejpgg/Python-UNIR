import numpy as np

# Array unidimensional
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Segmentación básica
primeros_tres = arr[0:3]  # [0, 1, 2]
del_segundo_al_quinto = arr[1:5]  # [1, 2, 3, 4]

# Omitir inicio o fin
desde_inicio = arr[:5]  # [0, 1, 2, 3, 4]
hasta_final = arr[5:]  # [5, 6, 7, 8, 9]

print(f"Primeros tres elementos: {primeros_tres}")
print(f"Del segundo al quinto: {del_segundo_al_quinto}")
print(f"Desde el inicio hasta el quinto: {desde_inicio}")
print(f"Desde el quinto hasta el final: {hasta_final}")















# Array unidimensional
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Seleccionar elementos alternos
elementos_pares = arr[::2]  # [0, 2, 4, 6, 8]
elementos_impares = arr[1::2]  # [1, 3, 5, 7, 9]

# Paso negativo (invierte el orden)
invertido = arr[::-1]  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
invertido_saltos = arr[::-2]  # [9, 7, 5, 3, 1]

print(f"Elementos en posiciones pares: {elementos_pares}")
print(f"Elementos en posiciones impares: {elementos_impares}")
print(f"Array invertido: {invertido}")
print(f"Array invertido con saltos de 2: {invertido_saltos}")













# Array 4D (2x3x4x2)
arr_4d = np.arange(48).reshape(2, 3, 4, 2)

# Acceder a todos los elementos de la primera "hiper-matriz"
# Equivalente a arr_4d[0, :, :, :]
primera_hipermatriz = arr_4d[0, ...]

# Acceder a la última dimensión del segundo elemento
# Equivalente a arr_4d[1, 2, 3, :]
ultimo_vector = arr_4d[1, 2, 3, ...]

print("Forma del array 4D:", arr_4d.shape)
print("Forma de la primera hipermatriz:", primera_hipermatriz.shape)
print("Último vector:", ultimo_vector)















import numpy as np

# Crear un array original
original = np.array([1, 2, 3, 4, 5])

# Crear una vista mediante segmentación
vista = original[1:4]  # [2, 3, 4]

# Modificar un elemento en la vista
vista[0] = 20

print("Array original después de modificar la vista:", original)  # [1, 20, 3, 4, 5]
print("Vista:", vista)  # [20, 3, 4]












# Operaciones que generalmente crean vistas:

# Segmentación básica (slicing)
vista1 = original[1:4]

# Cambio de forma sin modificar datos
vista2 = original.reshape(5, 1)  # Si es posible sin reordenar elementos

# Transposición simple
vista3 = original.T  # Para arrays 1D no tiene efecto visible



# Operaciones que generalmente crean copias:

# Copia explícita
copia1 = original.copy()

# Operaciones que cambian el tipo de datos
copia2 = original.astype(np.float64)

# Operaciones que reordenan elementos
copia3 = original[::-1]  # Aunque parece slice, reordena elementos













# Detectando si tenemos una vista o una copia

# Crear array original
original = np.array([1, 2, 3, 4, 5])

# Crear vista y copia
vista = original[1:4]
copia = original.copy()

# Verificar si comparten memoria
print("¿La vista comparte memoria con el original?", np.shares_memory(original, vista))  # True
print("¿La copia comparte memoria con el original?", np.shares_memory(original, copia))  # False

# Verificar si los datos son contiguos en memoria
print("¿Los datos de la vista son contiguos?", vista.flags.c_contiguous)

















