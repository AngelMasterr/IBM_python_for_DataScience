# primero instale el numpy: pip install numpy

import numpy as np

list_a = np.array([0, 1, 2, 3, 4])
list_b = np.array([1, 10, 20, 30, 40])
matriz_a = np.array([[0,1,2,3,4],[5,6,7,8,9]])
print(list_a)
print(matriz_a)

# atributos de numpy
print(len(list_a))  # len: tamaño de la lista metdodo tradicional = 5
print(list_a.size)  # size: tamaño de la lista de numpy = 5
print(list_a.ndim)  # ndim: es la dimension del arreglo = 1 : 1 fila y 1 columna (unidimensional)
# en una matriz cada array o lista corresponde a cada fila
print(matriz_a.ndim) # ndim: es la dimension del arreglo = 2 : 1 fila y 2 columnas (1, 2)
print(matriz_a.shape) # shape: es una tupla de enteros que indica el tamaño de la matriz = (2,5) 2 rows 5 columns

# cada lista de numero se toma como si fuera una columna, cada vez que agragamos una lista es como si agregaramos una columna a la matriz
print(list_a + 1)       # [1, 2, 3, 4, 5] = suma a cada elemento de la lista 1 
print(list_a + list_b)  # [ 1 11 22 33 44] = suma cada elemento segun su posicion de cada lista 
print(sum(matriz_a))    # [ 5  7  9 11 13] = suma cada elemento segun su posicion de cada lista o array de la matriz

# Esta manera es la forma clasica de sumar dos vecotres o listas, la cual conlleva a hace mas codigo
list_c = []
for i,j in zip(list_a, list_b):
    list_c.append(i + j)
print(list_c)

# Igualmente para multiplicar o dividir es mas facil con Numpy
print(2 * list_a)       # [0 2 4 6 8] = multiplica cada elemento de la lista por 2
print(list_a * list_b)  # [0 10 40 90 160] Multiplica las dos listas o arrays segun su posicion

# dot: multiplica las dos listas y luego suma su resultado
print(np.dot(list_a, list_b))   # [0 + 10 + 40 + 90 + 160] = 300

# mean: calcula la media de la lista
print(list_a.mean()) # [0 + 1 + 2 + 3 + 4]/5 = 10/5 = 2

# Otras funciones
print(list_a.max())     # imprime el valor maximo de la lista = 4
print(np.pi)            # imprime el numero pi = 3.141592653589793

# trabaja con lista o vectores que tengan el numero pi = 3.141592 = (180° = pi radianes)   
lista_rad = np.array([0, np.pi/2, np.pi])  # seria similar en grados a [0, 90°, 180°] 

# np.sin() = toma cada elemnto de la lista y lo pasa a seno
lista_sen = np.sin(lista_rad) #  = [sin(0), sin(90), sin(180)]
 
# es recomendable redondear el resultado, debido a que le respuesta tiene demasiado decimales
lista_sen = np.round(lista_sen,2) # round intenta redondear a los decimales deseados
print(lista_sen) # [0., 1., 0.,] el problema de round, es que cuando son tantos decimales repetidos no redonde al numero que se le da

# esta alternativa es mucho mejor para rendondear decimales a la cantidad deseada
cadena_sen = ' '.join("{:.2f}".format(x) for x in lista_sen)
print(cadena_sen)

# np.linespace(): crea una lista, indica donde empieza y termina y cuantos elemento va tener
lista_space = np.linspace(-2, 2, 9) # la lista empuiza en -2 y termina en 2 y tiene un recorrido de 9 elementos
print(lista_space) # [-2. -1.5 -1. -0.5  0.  0.5  1.  1.5  2.]