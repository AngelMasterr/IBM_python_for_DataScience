# Siempre que vayamos a escribir en un txt, es necesario que se encuentre vacio o de lo contrario se borrara todo 
# el contenido, debido a que "write" epieza en la primera linea, para que no pase eso hay que usar "add"

with open("prueba//prueba.txt","w") as ejemplo1:
    ejemplo1.write("la realidad es parte de una creencia o creación \n")
    ejemplo1.write("es infinita o tan solo no existe \nla percepcion de lo tangible puede cambiar \n")
    
# "a" : add agrega nuevas palabras al archivo existente no lo borra, como lo hace el write

with open("prueba//prueba.txt","a") as ejemplo1:  
    ejemplo1.write("entender como funciona la fisica es solo un constructo de la realidad impuesta \n")
    
    lineas = ["estudia \n", "investiga \n", "cuestionate todo \n"]
    for line in lineas:
        ejemplo1.write(line) 

    
with open("prueba//prueba.txt","r") as ejemplo1:   
    print(ejemplo1.read())
    