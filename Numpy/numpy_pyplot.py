# primero instale el matplotlib: pip install matplotlib

# Revise el archivo numpy_array.py que explica muchas cosas de como funciona el numpy
# REVISELO PERRO

import numpy as np
import matplotlib.pyplot as plt

# dibujar la funcion seno desde 0 hasta 2pi (0° - 360°)
# cree una lista de 100 elementos desde 0 hasta 2pi

list_x = np.linspace(0, 2*np.pi, 100) # esto crea una lista de 100 elementos desde 0 a 2pi
list_y = np.sin(list_x)               # esto multiplica cada elemento de la list_x por seno

# plot: este atributo de pyplot permite crear graficas con los datos introducidos
plt.plot(list_x, list_y)
plt.show()