# pandas: es mas practico que "open" y el diminutivo mas usado es "pd" 

# se debe instalar "pip" desde el terminal de window "cmd - adminstrador" (py -m ensurepip --upgrade)
# para verficar si quedo instalado y todo lo que tiene (py -m pip) 
# luego instalar pandas (py -m pip install pandas)

import pandas as pd
from openpyxl import workbook

xlsx_path = pd.read_excel("Archivos//1archivo_xlsx.xlsx")

# imprimir el nombre de las columnas
print(xlsx_path.columns)

# imprimir las columnas indicadas
print(xlsx_path[["nombre", "apellido"]])

# Imprimir la fila, columna o celda especificada
# iloc: es para llamar la celda de la tabla por su posicion row y column
# loc: se puedo llamar la celda por su row y name_column
print(xlsx_path.iloc[0,2])
print(xlsx_path.loc[0,"edad"])

# llamar un tramos de la tabla
print(xlsx_path.iloc[0:2,0:2]) # iloc llega hata -1 del valor indicado
print(xlsx_path.loc[0:2,"nombre":"apellido"]) # tenca en ceunta que loc si llega hasta el valor indicado

# DataFrame: es una estructura de datos tabular bidimensional que consta de filas y columnas etiquetadas. 
# En este caso, se ha creado un objeto DataFrame con dos columnas, 'a' y 'b', y tres filas, etiquetadas 
# como 0, 1 y 2. Las columnas 'a' y 'b' contienen los valores [11, 21, 31] y [21, 22, 23], respectivamente.
df = pd.DataFrame({'a':[11,21,31],'b':[21,22,23]})
print(df.head())

df = pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})
print(df['a']==1)