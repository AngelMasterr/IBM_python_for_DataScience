import numpy as np

list_a = np.array([0, 1, 2, 3, 4])
list_b = np.array([1, 10, 20, 30, 40])
matriz_a = np.array([[0,1,2,3,4],[5,6,7,8,9]])
print(list_a)
print(list_b)

# atributos de numpy
print(len(list_a))  # len: tamaño de la lista metdodo tradicional = 5
print(list_a.size)  # size: tamaño de la lista de numpy = 5
print(list_a.ndim)  # ndim: es la dimension o el rango de la matriz = 1
print(matriz_a.shape) # shape: es una tupla de enteros que indica el tamaño de la matriz en cada dimensión = (2,5) 2 colums 5 rows

# cada lista de numero se toma como si fuera una columna, cada vez que agragamos una lista es como si agregaramos una columna a la matriz
print(list_a + 1)       # suma a cada elemento de la lista 1 = [1, 2, 3, 4, 5]
print(list_a + list_b)  # suma cada elemento segun su posicion de cada lista = [ 1 11 22 33 44]
print(sum(matriz_a))    # suma cada elemento segun su posicion de cada lista del array = [ 5  7  9 11 13]

# Esta manera es la forma clasica de sumar dos vecotres o listas, la cual conlleva a hace mas codigo
list_c = []
for i,j in zip(list_a, list_b):
    list_c.append(i + j)
print(list_c)

# Igualmente para multiplicar o dividir es mas facil con Numpy
print(2 * list_a)       # No es necesario crear un bucle para que tome cada elemento y lo multiplique por 2
print(list_a * list_b)  # Multiplica cada elemento segun su posicion en la lista o vector

# dot: multiplica los vectores y luego suma su resultado
print(np.dot(list_a, list_b))   # [0 + 10 + 40 + 90 + 160] = 300

# mean: calcula la media de la lista
print(list_a.mean()) # [0 + 1 + 2 + 3 + 4]/5 = 10/5 = 2

# Otras funciones
print(list_a.max())     # imprime el valor maximo de la lista = 4
print(np.pi)            # imprime el numero pi = 3.141592653589793

# trabaja con lista o vectores que tengan el numero pi = 3.141592 = (180° = pi radianes)   
lista_rad = np.array([0, np.pi/2, np.pi])   # seria similar en grados a [0, 90°, 180°] 
lista_sen = np.sin(lista_rad) # np.sin() = toma cada elemnto de la lista y lo pasa a seno = [sin(0), sin(90), sin(180)] 
lista_sen = np.round(lista_sen,2) # es recomendable redondear el resultado, debido a que le respuesta tiene demasiado decimales
print(lista_sen)
