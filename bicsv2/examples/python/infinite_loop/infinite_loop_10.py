def floyd_warshall(graph):
    distance = list(map(lambda i: list(map(lambda j: j, i)), graph))
    k, i, j = 0, 0, 0
    while k < len(graph):
        while i < len(graph):
            while j < len(graph):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
            i += 1
        k += 1
    return distance
