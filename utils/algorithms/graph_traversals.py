from collections import deque
from typing import List, Any, Dict


class GraphTraversal:
    def __init__(self, graph: Dict[Any, List[Any]]):
        """
        Initialize with a graph adjacency list.
        :param graph: Dictionary mapping node to list of neighbors.
        """
        self.graph = graph

    def bfs(self, start: Any) -> List[Any]:
        """
        Perform Breadth-First Search (BFS) starting from the given node.
        :param start: The starting node for BFS.
        :return: List of nodes in the order they are visited.
        """
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

    def dfs(self, start: Any) -> List[Any]:
        """
        Perform Depth-First Search (DFS) starting from the given node.
        :param start: The starting node for DFS.
        :return: List of nodes in the order they are visited.
        """
        visited = set()
        traversal_order = []

        def _dfs(node):
            if node not in visited:
                visited.add(node)
                traversal_order.append(node)
                for neighbor in self.graph[node]:
                    _dfs(neighbor)

        _dfs(start)
        return traversal_order
