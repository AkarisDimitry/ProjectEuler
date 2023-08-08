import numpy as np
import networkx as nx
import matplotlib as plt
from functions import *
import math, copy

import time 
from functools import reduce

@timer
def P107() -> int: 
    '''
    The following undirected network consists of seven vertices and twelve edges with a total weight of 243.
    The same network can be represented by the matrix below.

            A   B   C   D   E   F   G
    A   -   16  12  21  -   -   -
    B   16  -   -   17  20  -   -
    C   12  -   -   28  -   31  -
    D   21  17  28  -   18  19  23
    E   -   20  -   18  -   -   11
    F   -   -   31  19  -   -   27
    G   -   -   -   23  11  27  -
    However, it is possible to optimise the network by removing some edges and still ensure that all points on the network remain connected. The network which achieves the maximum saving is shown below. It has a weight of 93, representing a saving of 243 − 93 = 150 from the original network.
    Using network.txt (right click and 'Save Link/Target As...'), a 6K text file containing a network with forty vertices, and given in matrix form, find the maximum saving which can be achieved by removing redundant edges whilst ensuring that the network remains connected.
    ''' 

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

    # Carga la red
    network = load_network("/home/akaris/Documents/code/Math/problems/ProjectEuler/files/problem107.txt")
    # Encuentra el árbol recubridor mínimo
    total = sum([ n2 if n2 < 100000 else 0 for n1 in network for n2 in n1 ])/2 
    saving = kruskal_MST(network)
    # Calcula el ahorro máximo
    saving = sum([n[2] for n in saving])

    return total - saving

P107()