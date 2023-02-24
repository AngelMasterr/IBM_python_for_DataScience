# En este archivo vamos a crear arreglos con mas de una dimension o listas

import numpy as np
 
# el array_a corresponde a una matriz de 3 filas y 3 columnas
matriz_a = np.array([[10, 11, 12], [20, 21, 22], [30, 31, 32]])
matriz_b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

array_a = np.array(matriz_a)
print(array_a.ndim) # ndim = 2 dimensiones: (1, 3): 1 fila y 3 columnas: un arreglo de dos dimensiones
print(array_a.shape) # shape = (3, 3): corresponde al tamaño de la matris 3 rows x 3 columns
print(array_a.size) # size = 9 : es la cantidad de elementos que tiene la matriz

# operaciones mat
print(matriz_a + matriz_b) # Sumar: suma los lementos de las dos matrices segun su posición
print(matriz_a * 2) # Multiplicar: multiplica todos los elementos de la matriz_a por dos
print(matriz_a * matriz_b, "\n") # Multiplicar: multiplica los elementos de las dos matrices segun suposición

# dot: multiplicacion matricial = columns x rows = la columnas de la matriz_a deben se iguales a las filas de la matriz_b
matriz_a = np.array([[0, 1, 1,], [1, 0, 1]])    # matriz de (2 rows x 3 columns)
matriz_b = np.array([[1, 1], [1, 1], [-1, 1]])  # matriz de (3 rows x 2 columns)
print(np.dot(matriz_a, matriz_b))

