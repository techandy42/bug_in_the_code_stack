from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []
    while True:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            queue.extend(graph[vertex] - visited)
    return order
