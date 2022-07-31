#Authors Kaio Guilherme, Wandressa Reis

class Grafo:
    
    def __init__(self, Vertices):
        self.Vertices = Vertices
        self.grafo = [[0]*self.Vertices for i in range(self.Vertices)]
    
    def adicionar_aresta(self, vertice1, vertice2, peso):
        self.grafo[vertice1 - 1][vertice2 - 1] = peso
        
    def imprimir_grafo(self):
        print("A matriz do grafo é:")
        for i in range(self.Vertices):
            print(self.grafo[i])

grafo = Grafo(4)
grafo.imprimir_grafo()

grafo.adicionar_aresta(1, 2, 1)
grafo.adicionar_aresta(1, 3, 1)
grafo.adicionar_aresta(2, 3, 1)


grafo.imprimir_grafo()  
