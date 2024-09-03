
from queue import Queue

class Vertice:
    def __init__(self, elemento, color, vecinos):
        self.elemento = elemento
        self.color = color
        self.vecinos = vecinos
    
    def setColor (self, color):
        self.color = color
    
    def getColor (self):
        return self.color
    
    def getElemento (self):
        return self.elemento
    
    def getVecinos (self):
        return self.getVecinos
    
    def setVecinos(self, vecinos):
        self.vecinos = vecinos
    
class Grafica:
    def __init__(self, nodos):
        vertices = {}
        for nodo, vecinos in nodos.items():
            vertice = Vertice(nodo, "B",vecinos)
            vertices[nodo] = vertice
        self.nodos = vertices
        
    def buscar(self, elemento):
            return self.nodos.get(elemento)

    def bfs_grafica (self, nodo):
        cola = Queue()
        recorrido = list()
        cola.put(nodo)
            
        while(not cola.empty()):
            vertice = cola.get()
            if vertice.color == "B":
                vertice.color = "N"
                recorrido.append(vertice)
                for vecino in vertice.vecinos:
                    encontrado = self.buscar(vecino)
                    cola.put(encontrado)
        print("el camino que genera la grafica es: ",end="")
        print("[",end="")
        for nodo in recorrido:
            print(nodo.elemento+", ",end="")
        print("]")              
            