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
    # Encuentra el árbol recubridor mínimo
    mst = kruskal(network)

    return maximum_saving(network, mst)

P107()