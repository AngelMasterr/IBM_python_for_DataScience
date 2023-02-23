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

