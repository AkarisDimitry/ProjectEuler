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

    # Carga la red
    network = load_network("/home/akaris/Documents/code/Math/problems/ProjectEuler/files/problem107.txt")

    saving = prim_MST(network)
    total = sum([ n2 if n2 < 100000 else 0 for n1 in network for n2 in n1 ])/2 
    saving = sum([ network[i][n] if i > 0 else 0 for i, n in enumerate(saving)])

    return total - saving

P107()