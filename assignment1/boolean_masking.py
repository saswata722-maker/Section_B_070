import numpy as np
matrix = np.arange(1,17).reshape(4,4)
con1 = matrix > 10
con2 = matrix % 2 == 0
result= matrix[con1 & con2]
print(result)