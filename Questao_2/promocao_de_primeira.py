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


entry = int(input(""))

pais = Grafo(entry)

for i in range(entry - 1):
    comand = input("")
    comand_char = comand.split(" ")
    comands = list(map(int, comand_char))
    pais.adicionar_aresta(comands[0], comands[1], (comands[2]+1))

pais.imprimir_grafo()
