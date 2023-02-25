# tomar una string y convertir desde el segundo caracter a mayuscula o minuscula si el caracter anterior se encuentra 
# antes en el alfabeto o despues
# ej: MonIcA = MOnica

import random
import string

# Creamos una funcion que cree palabras aleatorias de longitud len
def words_random(long):
    letters = string.ascii_letters # contenga solo letras ascii
    palabra = "".join(random.choices(letters,k=long))
    return palabra

# Converir las letraa a mayuscula o minusculas segun la letra anterior y su posicion en el alfabeto
alfa = "abcdefghijklmnopqrstuvwxyz"
ej = "npJeZpsz ajTfjDIlsWw" # = nPjeZpSZ
ej_low = ej.lower()

new_word:str = ej[0]
for i, j in zip((ej_low[1:]),(ej_low[:-1])):
    if j == " ": new_word += ej[len(new_word)] # Si hay palabras separadas por espcaio, la primera letra de cada palabra no se cambia
    elif alfa.find(i) > alfa.find(j):
        new_word += i.upper()
    elif alfa.find(i) < alfa.find(j):
        new_word += i.lower()
    else: new_word += i

print(ej)
print(new_word)
        
        
    