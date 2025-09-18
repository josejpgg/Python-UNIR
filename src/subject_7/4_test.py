import numpy as np

temperaturas = np.array([
    [25, 28, 30, 32, 29, 27, 26, 25, 24, 28, 31, 30, 29, 28, 27, 29, 30, 31, 32, 33, 34, 31, 29, 28, 27, 26, 25, 24, 25, 26],  # Ciudad A
    [18, 17, 19, 20, 21, 20, 19, 18, 17, 16, 15, 16, 17, 18, 19, 20, 21, 22, 21, 20, 19, 18, 17, 16, 15, 14, 15, 16, 17, 18],  # Ciudad B
    [31, 32, 33, 34, 35, 36, 35, 34, 33, 32, 31, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 38, 36, 34, 32, 30, 31, 32, 33]   # Ciudad C
])


for i, temp_ciudad in enumerate(temperaturas):
	print(f"--- Ciudad {i + 1} ---")
	print(f"Temperatura media: {temp_ciudad.mean()}")
	print(f"Temperatura maxima: {temp_ciudad.max()}")
	print(f"Temperatura minima: {temp_ciudad.min()}")
	print(f"Mediana de temperatura: {np.median(temp_ciudad)}")
	q1 = np.percentile(temp_ciudad, 25)
	q3 = np.percentile(temp_ciudad, 75)
	iqr = q3 - q1
	print(f"Rango intercuartilico: {iqr}")
	for j, temp_dia in enumerate(temp_ciudad):
		if temp_dia < q1 - 1.5 * iqr or temp_dia > q3 + 1.5 * iqr:
			print(f"Día {j + 1} con temperatura atípica: {temp_dia}")

