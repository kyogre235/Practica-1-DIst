from grafica import Grafica as G

# BFS algorithm
def bfs(grafica, nodo_inicio):
    grafo = G(grafica)
    vertice = grafo.buscar(nodo_inicio)
    
    if not vertice is None:
      grafo.bfs_grafica(vertice)
    else:
      print("el vertice no esta en la grafica")

# Llamamos a la funcion bfs

