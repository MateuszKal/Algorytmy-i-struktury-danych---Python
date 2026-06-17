import numpy as np
import random

def create_graph(nodes, saturation):
    graph = np.zeros((nodes, nodes))
    for i in range(nodes):
        for j in range(i+1, nodes):
            if random.random() < saturation:
                graph[i][j] = graph[j][i] = 1
    return graph

def create_hamiltonian_cycle(graph, nodes):
    cycle = list(range(nodes))
    random.shuffle(cycle)
    for i in range(nodes):
        graph[cycle[i]][cycle[(i+1)%nodes]] = graph[cycle[(i+1)%nodes]][cycle[i]] = 1
    return graph

def create_non_hamiltonian_graph(nodes):
    return create_graph(nodes, 0.5)

def isolate_node(graph, node):
    for i in range(len(graph)):
        graph[node][i] = 0
        graph[i][node] = 0
    return graph
