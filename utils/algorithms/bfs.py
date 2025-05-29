from collections import defaultdict, deque
from typing import List


class GraphTraversal:
    def __init__(self, graph):
        self.graph = graph

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        traversal_order = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                traversal_order.append(vertex)
                queue.extend(
                    neighbor
                    for neighbor in self.graph[vertex]
                    if neighbor not in visited
                )

        return traversal_order
