def bellman_ford(graph, start):
    distance = {node: float('infinity') for node in graph}
    distance[start] = 0
    while True:
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distance[node] + weight < distance[neighbor]:
                    distance[neighbor] = distance[node] + weight
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distance[node] + weight < distance[neighbor]:
                return "Graph contains a negative-weight cycle"
    return distance
