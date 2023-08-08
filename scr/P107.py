import numpy as np
import networkx as nx

def load_network(filename):
    # Cargar la red desde el archivo de texto
    network = []
    with open(filename, 'r') as file:
        for line in file:
            row = []
            for value in line.strip().split(','):
                if value == '-':
                    row.append(float('inf'))  # Representamos la distancia infinita con el valor infinito de Python
                else:
                    row.append(int(value))
            network.append(row)

    return network


def kruskal(network):
    # Crear un grafo a partir de la matriz de adyacencia
    G = nx.Graph()
    for i in range(len(network)):
        for j in range(i+1, len(network)):  # Solo necesitamos mirar la mitad superior de la matriz
            if network[i][j] != float('inf'):  # Solo añadimos la arista si la distancia no es infinita
                G.add_edge(i, j, weight=network[i][j])

    # Calcular el MST usando el algoritmo de Kruskal
    mst = nx.minimum_spanning_tree(G, algorithm='kruskal', weight='weight')

    return mst
# Definición de la clase Disjoint Set Union para manejar los conjuntos disjuntos
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] < self.rank[py]:
                self.parent[px] = py
            else:
                self.parent[py] = px
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1

def kruskal_MST(graph):
    # Número de vértices en el grafo
    V = len(graph)

    # Crear lista de aristas
    edges = []
    for i in range(V):
        for j in range(i+1, V):
            if graph[i][j] != 0:
                edges.append((graph[i][j], i, j))

    # Ordenar aristas por peso
    edges.sort()

    # Crear DSU
    dsu = DSU(V)

    # Crear lista para almacenar el MST
    mst = []

    # Agregar aristas al MST en orden, evitando ciclos
    for w, u, v in edges:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst.append((u, v, w))

    return mst


def prim_MST(graph):
    # Número de vértices en el grafo
    V = len(graph)
  
    # Inicializar con ceros
    mstSet = [0] * V
    key = [np.inf] * V
    parent = [None] * V  # Array para almacenar el árbol de expansión mínima
  
    # Hacer la llave 0 para que este vértice sea el primero
    key[0] = 0
    parent[0] = -1  # El primer nodo es la raíz del árbol de expansión mínima
  
    for _ in range(V):
        # Elegir el vértice de mínimo peso, del conjunto de vértices
        # aún no incluidos en el árbol de expansión mínima
        min_key = np.inf
        for v in range(V):
            if mstSet[v] == 0 and key[v] < min_key:
                min_key = key[v]
                u = v
  
        mstSet[u] = 1
  
        # Actualizar el valor de la llave de los vértices adyacentes al vértice elegido
        for v in range(V):
            if graph[u][v] > 0 and mstSet[v] == 0 and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u
  
    return parent


def maximum_saving(network, mst):
    # Calcular la suma de los pesos de todas las aristas
    total_weight = sum(network[i][j] for i in range(len(network)) for j in range(i+1, len(network)) if network[i][j] != float('inf'))

    # Calcular la suma de los pesos de las aristas en el MST
    mst_weight = sum(data['weight'] for u, v, data in mst.edges(data=True))

    # Calcular el ahorro
    saving = total_weight - mst_weight

    return saving


# Carga la red
network = load_network("/home/akaris/Documents/code/Math/problems/ProjectEuler/files/problem107.txt")

# Calcula el ahorro máximo
total = sum([ n2 if n2 < 100000 else 0 for n1 in network for n2 in n1 ])/2 
saving = kruskal_MST(network)
saving = sum([n[2] for n in saving])
print(total - saving)

saving = prim_MST(network)
total = sum([ n2 if n2 < 100000 else 0 for n1 in network for n2 in n1 ])/2 

saving = sum([ network[i][n] if i > 0 else 0 for i, n in enumerate(saving)])
print(total - saving)
# Encuentra el árbol recubridor mínimo
mst = kruskal(network)

# Calcula el ahorro máximo
saving = maximum_saving(network, mst)

print(saving)
