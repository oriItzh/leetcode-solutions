from collections import deque
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        """
        Problem: "Maximize the number of target Nodes after connecting Trees 1" ; leetcode #3372

        There exist two undirected trees with n and m nodes, with distinct labels in ranges [0, n - 1] and [0, m - 1], respectively.
        You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively,
        where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree
        and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree. You are also given an integer k.
        Node u is target to node v if the number of edges on the path from u to v is less than or equal to k. Note that a node is always target to itself.

        Return an array of n integers answer, where answer[i] is the maximum possible number of nodes target to node i of the first tree
        if you have to connect one node from the first tree to another node in the second tree.
        Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.
        """

        # Helper function to build adjacency list from edge list
        def build_adj(edges, n):
            # Create adjacency list for n nodes (0-indexed)
            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        # BFS to count number of nodes within distance k from src
        def _bfs_with_limit(src, isOne, k):
            # Select adjacency list for the correct tree
            adj = adj1 if isOne else adj2
            level = 0
            count = 0
            visited = set([src])
            q = deque([src])
            while level <= k and q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    count += 1
                    for nei in adj[cur]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
                level += 1
            return count

        # Number of nodes in each tree
        N, M = len(edges1) + 1, len(edges2) + 1
        # Build adjacency lists for both trees
        adj1, adj2 = build_adj(edges1, N), build_adj(edges2, M)

        # For each node in tree2, compute the max number of nodes reachable within (k-1) steps
        # This is because the connecting edge will use 1 step, so only (k-1) steps left in tree2
        max_reachable2 = max(_bfs_with_limit(src, 0, k - 1) for src in range(M))

        # For each node in tree1, compute the number of nodes reachable within k steps in tree1,
        # plus the maximum possible nodes reachable in tree2 (from any node) within (k-1) steps
        return [_bfs_with_limit(src, 1, k) + max_reachable2 for src in range(N)]


# Time Complexity Analysis:
# Let n = number of nodes in tree1, m = number of nodes in tree2.
# - build_adj: O(n + m) to build adjacency lists.
# - _bfs_with_limit: Each BFS is O(V + E) for the respective tree, but since trees have E = V - 1, it's O(V).
# - max_reachable2: Runs BFS from every node in tree2, so O(m * m).
# - The final list comprehension runs BFS from every node in tree1, so O(n * n).
# Total: O(m^2 + n^2), which is efficient for n, m <= 1000.

# Example 1:
# Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2
# Output: [9,7,9,8,8]

# Explanation:

# For i = 0, connect node 0 from the first tree to node 0 from the second tree.
# For i = 1, connect node 1 from the first tree to node 0 from the second tree.
# For i = 2, connect node 2 from the first tree to node 4 from the second tree.
# For i = 3, connect node 3 from the first tree to node 4 from the second tree.
# For i = 4, connect node 4 from the first tree to node 4 from the second tree.

# Example 2:

# Input: edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]], k = 1

# Output: [6,3,3,3,3]

# Explanation:

# For every i, connect node i of the first tree with any node of the second tree.


# Constraints:

# 2 <= n, m <= 1000
# edges1.length == n - 1
# edges2.length == m - 1
# edges1[i].length == edges2[i].length == 2
# edges1[i] = [ai, bi]
# 0 <= ai, bi < n
# edges2[i] = [ui, vi]
# 0 <= ui, vi < m
# The input is generated such that edges1 and edges2 represent valid trees.
# 0 <= k <= 1000
