import pandas as pd
import numpy as np

# Creamos un DataFrame de ejemplo con datos de ventas
datos = {
    'producto': ['Laptop', 'Teléfono', 'Tablet', 'Monitor', 'Teclado'],
    'precio': [1200, 800, 350, 250, 100],
    'stock': [15, 25, 40, 30, 50],
    'categoría': ['Computación', 'Móviles', 'Móviles', 'Periféricos', 'Periféricos']
}

df = pd.DataFrame(datos)
print(df)





# Crear una condición booleana
productos_caros = df['precio'] > 500

# Ver la serie booleana resultante
print(productos_caros)

# Aplicar el filtro al DataFrame
print(df[productos_caros])

# Todo en una sola línea
print(df[df['precio'] > 500])








# Equivalente a df[df['precio'] > 500]
resultado = df.query('precio > 500')
print(resultado)

# Condiciones múltiples
resultado = df.query('precio > 300 and stock < 30')
print(resultado)



# Usando operadores lógicos
resultado = df.query('categoría == "Móviles" or precio < 200')
print(resultado)

# Usando not
resultado = df.query('not (categoría == "Periféricos")')
print(resultado)










# Definimos variables externas
precio_limite = 400
categorias_interes = ['Móviles', 'Computación']

# Usamos las variables en la consulta
resultado = df.query('precio < @precio_limite and categoría in @categorias_interes')
print(resultado)














# where()


# Reemplazar salarios menores a 55000 con NaN
resultado = df['salario'].where(df['salario'] >= 55000)
print(resultado)

# Reemplazar salarios menores a 55000 con 50000
resultado = df['salario'].where(df['salario'] >= 55000, 50000)
print(resultado)








# Condiciones específicas por columna
condiciones = {
    'salario': df['salario'] > 55000,
    'experiencia': df['experiencia'] >= 5
}

# Crear un DataFrame con las mismas dimensiones
mascara = pd.DataFrame(condiciones, index=df.index)

# Aplicar where con la máscara
resultado = df.where(mascara, "No cumple")
print(resultado)









# mask()


# Reemplazar salarios mayores o iguales a 55000 con NaN
resultado = df['salario'].mask(df['salario'] >= 55000)
print(resultado)

# Reemplazar salarios mayores o iguales a 55000 con 55000 (aplicar un tope)
resultado = df['salario'].mask(df['salario'] >= 55000, 55000)
print(resultado)



# Censurar nombres de empleados con salarios altos
resultado = df['nombre'].mask(df['salario'] > 60000, "***")
print(resultado)











# isin()

# Filtrar empleados de departamentos específicos
departamentos_objetivo = ['IT', 'Finanzas']
filtro = df['departamento'].isin(departamentos_objetivo)
print(filtro)
print(df[filtro])
















import pandas as pd
import numpy as np

# Creamos un DataFrame con datos de productos
datos = {
    'producto': ['Monitor', 'Teclado', 'Mouse', 'Laptop', 'Tablet'],
    'precio': [250, 80, 45, 1200, 350],
    'stock': [30, 120, 150, 15, 40],
    'fecha_ingreso': pd.to_datetime(['2023-05-15', '2023-02-10', 
                                     '2023-03-22', '2023-01-05', '2023-04-18'])
}

df = pd.DataFrame(datos)
print(df)

# Ordenar por precio (ascendente por defecto)
df_ordenado = df.sort_values('precio')
print(df_ordenado)

# Ordenar por precio en orden descendente
df_ordenado_desc = df.sort_values('precio', ascending=False)
print(df_ordenado_desc)




# Ordenar primero por stock (ascendente) y luego por precio (descendente)
df_multi_orden = df.sort_values(['stock', 'precio'], ascending=[True, False])
print(df_multi_orden)











# Creamos un DataFrame con algunos valores nulos
df_con_nulos = df.copy()
df_con_nulos.loc[1, 'precio'] = np.nan
df_con_nulos.loc[3, 'stock'] = np.nan

# Ordenar con nulos al final (comportamiento predeterminado)
ordenado_nulos_final = df_con_nulos.sort_values('precio', na_position='last')
print(ordenado_nulos_final)

# Ordenar con nulos al principio
ordenado_nulos_inicio = df_con_nulos.sort_values('precio', na_position='first')
print(ordenado_nulos_inicio)
















# Crear un DataFrame con un índice no ordenado
df_indice = df.set_index('producto')
df_indice_desordenado = df_indice.reindex(['Laptop', 'Mouse', 'Tablet', 'Monitor', 'Teclado'])
print(df_indice_desordenado)

# Ordenar por índice (alfabéticamente en este caso)
df_indice_ordenado = df_indice_desordenado.sort_index()
print(df_indice_ordenado)

# Ordenar por índice en orden descendente
df_indice_desc = df_indice_desordenado.sort_index(ascending=False)
print(df_indice_desc)




# Ordenar índice con opciones adicionales
df_indice_con_nulos = df_indice_desordenado.copy()
df_indice_con_nulos.rename(index={'Laptop': None}, inplace=True)

ordenado_indice = df_indice_con_nulos.sort_index(ascending=False, na_position='first')
print(ordenado_indice)






















import pandas as pd
import numpy as np

# Creamos un DataFrame con datos de estudiantes
datos = {
    'estudiante': ['Ana', 'Carlos', 'Elena', 'David', 'Beatriz', 'Fernando'],
    'matemáticas': [85, 92, 78, 92, 88, 73],
    'ciencias': [90, 85, 95, 89, 92, 70],
    'literatura': [92, 78, 96, 85, 91, 84]
}

df = pd.DataFrame(datos)
print(df)



# rank()
# El método rank() asigna un rango o posición relativa a cada valor dentro de una Serie o DataFrame. Por defecto, asigna rangos en orden ascendente (el valor más pequeño recibe el rango 1):

# Ranking de calificaciones de matemáticas
ranking_matematicas = df['matemáticas'].rank()
print(ranking_matematicas)


# Ranking descendente (el valor más alto recibe el rango 1)
ranking_desc = df['matemáticas'].rank(ascending=False)
print(ranking_desc)








# 'average': Asigna el promedio de las posiciones a los valores empatados (método predeterminado).
# 'min': Asigna la posición más baja a todos los valores empatados.
# 'max': Asigna la posición más alta a todos los valores empatados.
# 'first': Asigna posiciones según el orden de aparición en los datos.
# 'dense': Similar a 'min', pero sin "huecos" en los rangos después de los empates.


# Observamos que Carlos y David tienen la misma calificación en matemáticas (92)
print(df[['estudiante', 'matemáticas']])

# Diferentes métodos para manejar empates
print("\nMétodo 'average' (predeterminado):")
print(df['matemáticas'].rank(method='average'))

print("\nMétodo 'min':")
print(df['matemáticas'].rank(method='min'))

print("\nMétodo 'max':")
print(df['matemáticas'].rank(method='max'))

print("\nMétodo 'first':")
print(df['matemáticas'].rank(method='first'))

print("\nMétodo 'dense':")
print(df['matemáticas'].rank(method='dense'))
















# nlargest()

# Obtener los 3 estudiantes con mejores calificaciones en matemáticas
mejores_matematicas = df.nlargest(3, 'matemáticas')
print(mejores_matematicas)

# Obtener los 3 mejores estudiantes considerando primero matemáticas y luego ciencias
mejores_estudiantes = df.nlargest(3, ['matemáticas', 'ciencias'])
print(mejores_estudiantes)










# nsmallest()

# Obtener los 2 estudiantes con calificaciones más bajas en literatura
peores_literatura = df.nsmallest(2, 'literatura')
print(peores_literatura)

# Obtener los 2 estudiantes con peores calificaciones considerando primero ciencias y luego matemáticas
estudiantes_apoyo = df.nsmallest(2, ['ciencias', 'matemáticas'])
print(estudiantes_apoyo)















