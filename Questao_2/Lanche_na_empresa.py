#Authors Kaio Guilherme, Wandressa Reis

class Grafo:

    def __init__(self, Vertices):
        self.Vertices = Vertices
        self.grafo = [[0]*self.Vertices for i in range(self.Vertices)]

    def adicionar_aresta(self, vertice1, vertice2, peso):
        self.grafo[vertice1 - 1][vertice2 - 1] = peso
        self.grafo[vertice2 - 1][vertice1 - 1] = peso

    def get_matriz(self):
        return self.grafo
    
    def imprimir_grafo(self):
        print("A matriz do grafo é:")
        for i in range(self.Vertices):
            print(self.grafo[i])


entry = input("")
comand_char = entry.split(" ")
comand = list(map(int, comand_char))

empresa = Grafo(comand[0])

for i in range(comand[1]):
    entry = input("")
    comand_char = entry.split(" ")
    comands = list(map(int, comand_char))
    empresa.adicionar_aresta(comands[0], comands[1], comands[2])

#empresa.imprimir_grafo()

melhor_sala = 0
menor_peso = 101
peso_total = 0
num_zero = 0

for vertice in range(comand[0]):
    if(melhor_sala == 0):
        melhor_sala = vertice + 1
    for i in range(comand[0]):
        if(empresa.grafo[vertice][i] == 0):
            num_zero += 1
        if(empresa.grafo[vertice][i] != 0):
            peso_total += empresa.grafo[vertice][i]
    if(peso_total < menor_peso and num_zero < (comand[0] - 2)):
        melhor_sala = vertice + 1
    num_zero = 0
            
#print(melhor_sala)
distancia = max(D for D in empresa.grafo[melhor_sala - 1] if D != 0)
print(distancia)