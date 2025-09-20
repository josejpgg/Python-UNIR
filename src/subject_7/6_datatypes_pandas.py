import pandas as pd
import numpy as np

# Crear un DataFrame de ejemplo
df = pd.DataFrame({
    'enteros': [1, 2, 3, 4, 5],
    'flotantes': [1.1, 2.2, 3.3, 4.4, 5.5],
    'texto': ['a', 'b', 'c', 'd', 'e'],
    'booleanos': [True, False, True, False, True]
})

# Verificar los tipos de datos
print(df.dtypes)








# Convertir enteros a flotantes
df['enteros_float'] = df['enteros'].astype('float64')

# Convertir flotantes a enteros (se pierden los decimales)
df['flotantes_int'] = df['flotantes'].astype('int64')

# Convertir números a strings
df['enteros_str'] = df['enteros'].astype(str)

print(df.dtypes)



# Convertir múltiples columnas
df = df.astype({
    'enteros': 'float32',
    'texto': 'string'  # Pandas 1.0+ tiene un tipo string dedicado
})

print(df.dtypes)











# Convertir a tipo categórico
df['ciudad_cat'] = df['ciudad'].astype('category')
df['valoracion_cat'] = df['valoracion'].astype('category')

# Crear categorías ordenadas (útil para variables ordinales)
df['valoracion_ordenada'] = pd.Categorical(
    df['valoracion'], 
    categories=['Baja', 'Media', 'Alta'], 
    ordered=True
)

# Comparaciones con categorías ordenadas
print(df[df['valoracion_ordenada'] > 'Baja'].head())













# El método pd.to_numeric() es especialmente útil para conversiones con posibles errores:

# DataFrame con valores problemáticos
df_problematico = pd.DataFrame({
    'mixto': ['1', '2', 'tres', '4', '5'],
    'con_nulos': [1.1, 2.2, None, 4.4, 5.5]
})

# Diferentes opciones de manejo de errores
print("Ignorar errores (mantener originales):")
print(pd.to_numeric(df_problematico['mixto'], errors='ignore'))

print("\nConvertir a NaN los valores problemáticos:")
print(pd.to_numeric(df_problematico['mixto'], errors='coerce'))

print("\nForzar downcast a menor tipo posible:")
print(pd.to_numeric(df_problematico['mixto'], errors='coerce', downcast='integer'))










# Impacto en la memoria y rendimiento

# Crear DataFrames para comparar uso de memoria
df_int = pd.DataFrame({'enteros': [1, 2, 3, 4, 5]})
df_int_con_na = pd.DataFrame({'enteros_con_na': [1, 2, None, 4, 5]})

print(f"Tipo sin valores nulos: {df_int['enteros'].dtype}")
print(f"Tipo con valores nulos: {df_int_con_na['enteros_con_na'].dtype}")

# Comparar uso de memoria
print(f"Memoria sin nulos: {df_int.memory_usage(deep=True).sum()} bytes")
print(f"Memoria con nulos: {df_int_con_na.memory_usage(deep=True).sum()} bytes")
















import pandas as pd
import numpy as np

# Crear un DataFrame con valores faltantes
df = pd.DataFrame({
    'A': [1, np.nan, 3, None, 5],
    'B': ['a', 'b', None, np.nan, 'e'],
    'C': [True, False, None, np.nan, True]
})

print(df)










# Detectar valores faltantes
print("\nDetección de valores faltantes:")
print(df.isna())  # También: df.isnull()

# Detectar valores no faltantes
print("\nDetección de valores no faltantes:")
print(df.notna())  # También: df.notnull()

# Contar valores faltantes por columna
print("\nCantidad de valores faltantes por columna:")
print(df.isna().sum())

# Verificar si alguna columna tiene al menos un valor faltante
print("\n¿Alguna columna tiene valores faltantes?")
print(df.isna().any())

# Verificar si todas las columnas tienen al menos un valor faltante
print("\n¿Todas las columnas tienen valores faltantes?")
print(df.isna().all())















# Crear un DataFrame para mostrar diferencias
df_diff = pd.DataFrame({
    'con_nan': [1, np.nan, 3],
    'con_none': [1, None, 3]
})

print(df_diff)
print(df_diff.dtypes)


# NaN es un valor de punto flotante especial de NumPy
# None es un objeto de Python
# Cuando se insertan en un DataFrame, Pandas puede convertir None a NaN en columnas numéricas

















# Crear una serie de fechas
fechas = pd.Series(pd.date_range('2023-01-01', periods=6, freq='D'))
print(f"Tipo de datos: {fechas.dtype}")
print(fechas)

# Crear un DataFrame con fechas
df_fechas = pd.DataFrame({
    'fecha': pd.date_range('2023-01-01', periods=6, freq='D'),
    'valor': np.random.randn(6)
})






# Extraer componentes de las fechas
df_fechas['año'] = df_fechas['fecha'].dt.year
df_fechas['mes'] = df_fechas['fecha'].dt.month
df_fechas['día'] = df_fechas['fecha'].dt.day
df_fechas['día_semana'] = df_fechas['fecha'].dt.day_name()

print(df_fechas)




# Operaciones aritméticas con fechas
df_fechas['fecha_siguiente'] = df_fechas['fecha'] + pd.Timedelta(days=1)
df_fechas['diferencia_días'] = (df_fechas['fecha_siguiente'] - df_fechas['fecha']).dt.days

# Filtrar por rango de fechas
periodo_medio = df_fechas[(df_fechas['fecha'] >= '2023-01-02') & 
                          (df_fechas['fecha'] <= '2023-01-04')]
print(periodo_medio)




















