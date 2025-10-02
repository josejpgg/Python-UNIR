import numpy as np
import pandas as pd


arr = np.arange(0, 10, 2)

print(np.ones((3, 3)))



tmp = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
	'B': [10, 20, 30, 40, 50]
})

print(tmp[0:5])
