# Algoritmo de Busca em Profundidade 
# #
graph = {
    '2' : ['3'],
    '3' : ['5', '6', '4'],
    '5' : ['7', '6'], 
    '6' : ['8'],
    '4' : ['6'],
    '7' : ['8'],
    '6' : ['8'],
    '8' : []
}

visited = set() 

def dfs(visited, graph, node): 
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, '2') 
