import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
# Uma função utilitária para imprimir o MST conntruído armazenado em parent[] #
    def printMST(self, parent):
        print('Edge \tWeight')
        for i in range(1, self.V):
            print(parent[i], '-', i, '\t', self.graph[i][parent[i]])

# Uma função de utilidade para encontrar o vértice 
# com valor de distância mínima, a partir do conjunto 
# de vértices ainda não incluídos na árvore do caminho 
# mais curto #

    def minkey(self, key, mstSet):

        # Inicializa o valor mínimo
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        
        return min_index

# Função para contruir e imprimir MST para um gráfico 
# representado usando a representação da matriz #

    def primMST(self):
        # Valores chave usados para escolher a aresta de peso 
        # mínimo no corte #
        key = [sys.maxsize] * self.V
        parent = [None] * self.V # Array para armazenar o MST construído
        # Torna a chave vazia para que este vértice seja escolhido como primeiro vértice
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1 # O primeiro nó é sempre a raiz

        for cout in range(self.V):

            u = self.minkey(key, mstSet)

            mstSet[u] = True

            for v in range(self.V):

                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        
        self.printMST(parent)

g = Graph(5)
g.graph = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
g.primMST();