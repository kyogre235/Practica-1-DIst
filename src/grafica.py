
from queue import Queue

class Vertice:
    """
    clase que genera el vertice
    """
    def __init__(self, elemento, color, vecinos):
        """costructor de Vertice

        Args:
            elemento (str): el identificador del vertice
            color (str): caracter con el color del vertice (puede ser 'N' o 'B')
            vecinos (list): lista con los identificaderes de los vecinos
        """
        self.elemento = elemento
        self.color = color
        self.vecinos = vecinos
    
    def setColor (self, color):
        """cambia el color del vertice

        Args:
            color (str): color del vertice ('B' o 'N')
        """
        self.color = color
    
    def getColor (self):
        """regresa el color del vertice

        Returns:
            str: color del vertice ('B' o 'N')
        """
        return self.color
    
    def getElemento (self):
        """genera el identificador del vertice

        Returns:
            str: identificador del vertice
        """
        return self.elemento
    
    def getVecinos (self):
        """regresa la lista de vecinos

        Returns:
            list: la lista de los vecinos
        """
        return self.getVecinos
    
    
class Grafica:
    """
    clase que genera un a grafica con 
    """
    def __init__(self, nodos):
        """constructor de grafica

        Args:
            nodos (dict): diccionario que guarda los vertices de la grafica
        """
        vertices = {}
        for nodo, vecinos in nodos.items():
            vertice = Vertice(nodo, "B",vecinos)
            vertices[nodo] = vertice
        self.nodos = vertices
        
    def buscar(self, elemento):
        """busca en el diccionario de vertices si esta el elemento que buscamos

        Args:
            elemento (str): la llave con la que guardamos el vertice

        Returns:
            Vertice: si el elemento esta en el diccionario, None en otro caso
        """
        return self.nodos.get(elemento)

    def bfs_grafica (self, nodo):
        """clase que a partir de un vertice dado, 
        hace un recorrido bfs en la grafica e imprime el recorrido

        Args:
            nodo (str): el vertice donde va a comenzar el recorrido
        """
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
            