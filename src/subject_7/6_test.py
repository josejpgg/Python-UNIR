# Crea un DataFrame con las siguientes columnas: 'edad' (valores enteros), 'altura' (valores decimales), 'nombre' (texto) y 'activo' (booleanos). Luego realiza las siguientes tareas:

# Verifica y muestra los tipos de datos de todas las columnas usando el atributo dtypes
# Convierte la columna 'edad' a tipo float64
# Convierte la columna 'altura' a tipo int64
# Convierte la columna 'nombre' a tipo category
# Muestra nuevamente los tipos de datos para verificar los cambios
# Calcula y muestra el uso de memoria del DataFrame antes y después de las conversiones usando memory_usage(deep=True)

import pandas as pd
import numpy as np

df = pd.DataFrame(
	{
		'edad': np.random.randint(18, 70, size=5),
		'altura': np.random.uniform(1.5, 2.0, size=5).round(2),
		'nombre': np.random.choice(['Ana', 'Luis', 'Marta', 'Carlos', 'Sofía'], size=5),
		'activo': np.random.choice([True, False], size=5)
	}
)
df = df.astype({'edad': 'int32', 'altura': 'float32', 'nombre': 'string', 'activo': 'bool'})

print(f"Tipo de datos originals:\n{df.dtypes}")
print(f"Uso de memoria original: {df.memory_usage(deep=True).sum()} bytes\n")

df['edad'] = df['edad'].astype('float64')
df['altura'] = df['altura'].astype('int64')
df['nombre'] = df['nombre'].astype('category')

print(f"Tipo de datos cambiado:\n{df.dtypes}")
print(f"Uso de memoria cambiado: {df.memory_usage(deep=True).sum()} bytes")
