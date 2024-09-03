
import sys
import re
from BFS import bfs

lista = list()
dicc={}
patron = r'^([A-Z](?![A-Z])(:[A-Z](?![A-Z]))?(,[A-Z](?![A-Z]))*)$'


if len(sys.argv) > 1:
    
    for i in range(1,len(sys.argv)):
        if re.fullmatch(patron,sys.argv[i]):
            arg = sys.argv[i]
            args = arg.split(":",1)
            for char in args[1]:
                if not char == ',':
                    lista.append(char)
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
    print("no hay argumentos pa")


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