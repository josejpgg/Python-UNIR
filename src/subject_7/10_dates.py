import pandas as pd
import numpy as np

# Convertir una cadena simple a datetime
fecha = pd.to_datetime('2023-05-15')
print(fecha)







# Formato personalizado usando códigos de formato de datetime
fecha_personalizada = pd.to_datetime('15-05-2023 14:30:25', format='%d-%m-%Y %H:%M:%S')
print(fecha_personalizada)












# Lista con una fecha inválida
fechas_con_error = ['2023-01-15', 'no es una fecha', '2023-03-10']

# Por defecto, lanza un error
try:
    pd.to_datetime(fechas_con_error)
except Exception as e:
    print(f"Error: {e}")

# Con errors='coerce', convierte valores inválidos a NaT (Not a Time)
fechas_corregidas = pd.to_datetime(fechas_con_error, errors='coerce')
print(fechas_corregidas)

# Con errors='ignore', deja los valores inválidos sin cambios
fechas_ignoradas = pd.to_datetime(fechas_con_error, errors='ignore')
print(fechas_ignoradas)













# Crear una fecha con zona horaria específica
fecha_con_tz = pd.to_datetime('2023-05-15 14:30:00').tz_localize('Europe/Madrid')
print(fecha_con_tz)

# Convertir a otra zona horaria
fecha_nueva_tz = fecha_con_tz.tz_convert('America/New_York')
print(fecha_nueva_tz)
















# Crear un rango de fechas básico (diario por defecto)
fechas_diarias = pd.date_range(start='2023-01-01', end='2023-01-10')
print(fechas_diarias)








# Rango de fechas mensuales
fechas_mensuales = pd.date_range(start='2023-01-01', end='2023-12-31', freq='M')
print(fechas_mensuales)

# Rango de fechas semanales (cada lunes)
fechas_semanales = pd.date_range(start='2023-01-01', end='2023-03-01', freq='W-MON')
print(fechas_semanales)

# Rango de fechas con horas (cada 6 horas)
fechas_horas = pd.date_range(start='2023-01-01', periods=5, freq='6H')
print(fechas_horas)













