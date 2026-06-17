def find_euler_cycle(graph): 
    degrees = [sum(row) for row in graph]
    if any(degree % 2 != 0 for degree in degrees):
        return None 
    cycle = []
    stack = [0]
    while stack:
        vertex = stack[-1]
        if degrees[vertex]:
            for neighbor, edge in enumerate(graph[vertex]):
                if edge:
                    stack.append(neighbor)
                    graph[vertex][neighbor] = graph[neighbor][vertex] = 0
                    degrees[vertex] -= 1
                    degrees[neighbor] -= 1
                    break
            else:
                cycle.append(stack.pop())
        else:
            cycle.append(stack.pop())
    return cycle[::-1]

def is_valid(v, pos, path, graph):
    if v >= len(graph):
        return False
    if graph[path[pos-1]][v] == 0 or v in path:
        return False
    return True

def hamilton_cycle_util(graph, path, pos):
    if pos == len(graph):
        return graph[path[pos-1]][path[0]] == 1
    for v in range(1, len(graph)):
        if pos < len(graph) and is_valid(v, pos, path, graph):
            path[pos] = v
            if hamilton_cycle_util(graph, path, pos + 1):
                return True
            path[pos] = -1
    return False

def find_hamilton_cycle(graph):
    path = [-1] * len(graph)
    path[0] = 0
    if not hamilton_cycle_util(graph, path, 1):
        return None
    return path