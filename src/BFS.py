from grafica import Grafica as G

# BFS algorithm
def bfs(grafica, nodo_inicio):
  """funcion que crea la grafica y hace dfs con el elemento que le mandes

  Args:
      grafica (dict): el diccionario con los vertices
      nodo_inicio (str): el nodo donde se quiere empezar 
  """
  grafo = G(grafica)
  vertice = grafo.buscar(nodo_inicio)
    
  if not vertice is None:
    grafo.bfs_grafica(vertice)
  else:
    print("el vertice no esta en la grafica")

# Llamamos a la funcion bfs

