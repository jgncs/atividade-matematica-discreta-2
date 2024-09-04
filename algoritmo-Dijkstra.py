Grafo = {
    "A": {"T": 118, "Z": 75, "S": 140},
    "T": {"A": 118, "L": 111},
    "Z": {"A": 75, "O": 71},
    "S": {"A": 140, "F": 99, "R": 80},
    "L": {"T": 111, "M": 70},
    "O": {"Z": 71, "S": 151},
    "F": {"S": 99, "B": 211},
    "R": {"S": 80, "P": 97, "C": 146},
    "M": {"L": 70, "D": 75},
    "P": {"R": 97, "B": 101, "C": 138},
    "B": {"P": 101, "F": 211, "G": 90},
    "D": {"M": 75, "C": 120, "P": 138},
    "C": {"D": 120, "R": 146},
    "G": {"B": 90}
}

    
def Dijkstra(Grafo, origem):
    #criar uma lista de vertices 
    Q = [v for v in Grafo]

    #cria uma lista de predecessores e distancia
    predecessor = {v: 'und' for v in Q} 
    distancia = {v: float('inf') for v in Q}

    distancia[origem] = 0

    vertice_atual = origem

    predecessor[origem] = origem

    while len(Q) > 0:
        #seleciona o vértice com menor distância 
        s = float('inf')
        for u in Q:
            if distancia[u] < s:
                s = distancia[u]
                vertice_atual = u
        
        #o vertice_atual será o que tem menor distância 
        
        #remove vertice_atual da lista Q:     
        Q.remove(vertice_atual)

        for vizinho, peso in Grafo[vertice_atual].items():
            alt = distancia[vertice_atual] + peso

            if alt < distancia[vizinho]:
                distancia[vizinho] = alt
                predecessor[vizinho] = vertice_atual

    return distancia, predecessor


dist, predecessor = Dijkstra(Grafo, 'A')

print(dist)
print('----------------')
print(predecessor)



## caminho mínimo 

def caminho_minimo(origem, destino):

    dist, prev = Dijkstra(Grafo, origem)
    
    caminho = []
    caminho.append(destino)

    v = destino
    while v != origem:
        v = predecessor[v]
        caminho.append(v)

    caminho.reverse()

    return caminho


caminho = caminho_minimo ('A', 'G')

print(caminho)