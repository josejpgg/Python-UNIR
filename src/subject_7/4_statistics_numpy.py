import numpy as np


# Matriz 2D que representa calificaciones de estudiantes en diferentes asignaturas
calificaciones = np.array([
    [85, 90, 78, 92],  # Estudiante 1
    [76, 88, 95, 87],  # Estudiante 2
    [91, 82, 89, 94]   # Estudiante 3
])

# Media por estudiante (a lo largo del eje 1)
media_estudiantes = np.mean(calificaciones, axis=1)
print("Media por estudiante:")
print(media_estudiantes)  # [86.25, 86.5, 89.0]

# Media por asignatura (a lo largo del eje 0)
media_asignaturas = np.mean(calificaciones, axis=0)
print("Media por asignatura:")
print(media_asignaturas)  # [84.0, 86.67, 87.33, 91.0]










# Mediana por estudiante
mediana_estudiantes = np.median(calificaciones, axis=1)
print("Mediana por estudiante:")
print(mediana_estudiantes)  # [87.5, 87.5, 90.0]

# Mediana por asignatura
mediana_asignaturas = np.median(calificaciones, axis=0)
print("Mediana por asignatura:")
print(mediana_asignaturas)  # [85.0, 88.0, 89.0, 92.0]








datos = np.array([12, 15, 21, 18, 9, 24, 17, 22, 30, 25, 11, 14])


# Calcular el percentil 75 para cada asignatura
p75_asignaturas = np.percentile(calificaciones, 75, axis=0)
print("Percentil 75 por asignatura:")
print(p75_asignaturas)  # [88.0, 89.0, 92.0, 93.0]

# Calcular múltiples percentiles de una vez
percentiles = np.percentile(datos, [25, 50, 75, 90])
print("Múltiples percentiles:")
print(percentiles)  # [12.75, 17.5, 23.5, 27.5]











# Equivalente a percentile(datos, 25)
q25 = np.quantile(datos, 0.25)

# Equivalente a percentile(datos, [25, 50, 75])
quantiles = np.quantile(datos, [0.25, 0.5, 0.75])

print(f"Cuantil 0.25: {q25}")  # Output: Cuantil 0.25: 12.75
print("Múltiples cuantiles:")
print(quantiles)  # [12.75, 17.5, 23.5]














import numpy as np

# Dos conjuntos de datos con la misma media pero diferente dispersión
datos_a = np.array([10, 11, 9, 12, 8, 10, 10])
datos_b = np.array([2, 18, 5, 15, 10, 0, 20])

# Ambos tienen la misma media
print(f"Media de datos_a: {np.mean(datos_a)}")  # 10.0
print(f"Media de datos_b: {np.mean(datos_b)}")  # 10.0

# Pero diferente desviación estándar
std_a = np.std(datos_a)
std_b = np.std(datos_b)

print(f"Desviación estándar de datos_a: {std_a:.2f}")  # 1.29
print(f"Desviación estándar de datos_b: {std_b:.2f}")  # 7.48















# Calcular la varianza
var_a = np.var(datos_a)
var_b = np.var(datos_b)

print(f"Varianza de datos_a: {var_a:.2f}")  # 1.67
print(f"Varianza de datos_b: {var_b:.2f}")  # 56.00

# Verificar relación entre varianza y desviación estándar
print(f"Raíz cuadrada de la varianza de datos_a: {np.sqrt(var_a):.4f}")  # 1.2910
print(f"Desviación estándar de datos_a: {std_a:.4f}")                   # 1.2910
















# Datos en diferentes escalas
temperaturas_c = np.array([22, 24, 21, 25, 23])  # Celsius
precios = np.array([1200, 1350, 1100, 1400, 1250])  # Euros

# Calcular coeficientes de variación
cv_temp = (np.std(temperaturas_c) / np.mean(temperaturas_c)) * 100
cv_precios = (np.std(precios) / np.mean(precios)) * 100

print(f"CV temperaturas: {cv_temp:.2f}%")  # 6.52%
print(f"CV precios: {cv_precios:.2f}%")    # 9.13%

















