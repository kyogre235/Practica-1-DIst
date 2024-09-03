
import sys
import re
from BFS import bfs
#grafica de ejemplo:
grafica = {
  'A' : ['B','C', 'D', 'E'],
  'B' : ['A', 'C', 'G'],
  'C' : ['A', 'B', 'D'],
  'D' : ['H', 'E', 'A', 'C'],
  'E' : ['A', 'D', 'F'],
  'F' : ['G', 'E', 'H', 'I'],
  'G' : ['F', 'B'],
  'H' : ['F', 'D'],
  'I' : ['F']
}  
# creamos una lista vacia, un diccionario vacio y definimos una expresion regular
# que nos verfifica que cada argumento de la entrada tiene el formato deseado.
lista = list()
dicc={}
patron = r'^([A-Z](?![A-Z])(:[A-Z](?![A-Z]))?(,[A-Z](?![A-Z]))*)$'
# ejemplos validos:
# A:B,D,C,S
# B:C
# I:H

# verfificamos que nos han pasado argumentos, si hay mas de 1, 
# nos estan pasando los nodos, si no hay mas, se trabaja con la grafica de ejemplo
if len(sys.argv) > 1:
    
    for i in range(1,len(sys.argv)):
        # verificamos si el argumento cumple con la regex
        if re.fullmatch(patron,sys.argv[i]):
            arg = sys.argv[i]
            args = arg.split(":",1)
            # creamos la lista de vecinos y creamos un vertice
            for char in args[1]:
                if not char == ',':
                    lista.append(char)
            # creamos el diccionario para hacer la grafica
            dicc[arg[0]] = lista
        else: 
            print("esto no es un vertice valido")
        lista = list()
    nodo = input("dame el nodo de donde quieres empezar ")
    nodo = nodo.upper()
    elemento = dicc.get(nodo)
    if not elemento ==  None:
        bfs(dicc,nodo)
else:
    print("usaremos la grafica de ejemplo del archivo y empezaremos en el nodo A")
    bfs(grafica,'A')
