#Authors Kaio Guilherme, Wandressa Reis




#foi o mais proximo que eu consegui fazer com tal tempo dado
class Grafo:

    def __init__(self, Vertices):
        self.Vertices = Vertices
        self.grafo = [[0]*self.Vertices for i in range(self.Vertices)]

    def adicionar_aresta(self, vertice1, vertice2, peso):
        self.grafo[vertice1 - 1][vertice2 - 1] = peso + 1
        self.grafo[vertice2 - 1][vertice1 - 1] = peso + 1

    def get_matriz(self):
        return self.grafo

    def imprimir_grafo(self):
        print("A matriz do grafo é:")
        for i in range(self.Vertices):
            print(self.grafo[i])

def busca(matriz_adj, vertice, visitados ):
    visitados.append(vertice-1)
    linha = len(visitados) % 2
    for i in range(len(matriz_adj)):
        if matriz_adj[vertice-1][i] == (linha + 1) and i not in visitados:
            busca(matriz_adj, i+1, visitados)
            
    return len(visitados)        
    
entry = int(input(""))

pais = Grafo(entry)

for i in range(entry - 1):
    comand = input("")
    comand_char = comand.split(" ")
    comands = list(map(int, comand_char))
    pais.adicionar_aresta(comands[0], comands[1], (comands[2]+1))

pais.imprimir_grafo()

matriz = pais.get_matriz()
visitados = []

maior = 0
atual = 0
for cidade in range(entry):
    atual = busca(matriz, cidade + 1, visitados)
    print(visitados)
    visitados.clear()
    if atual > maior:
        maior = atual

print(maior)