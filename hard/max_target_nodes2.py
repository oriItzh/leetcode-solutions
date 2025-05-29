from collections import defaultdict, deque
from typing import List


class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> List[int]:
        """
        Problem: Maximize the number of target nodes after connecting trees 2; leetcode #3373

        There exist two undirected trees with n and m nodes, labeled from [0, n - 1] and [0, m - 1], respectively.
        You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively,
        where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree
        and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.
        Node u is target to node v if the number of edges on the path from u to v is even.
        Note that a node is always target to itself.
        Return an array of n integers answer, where answer[i] is the maximum possible number of nodes that are target to node i of the first tree
        if you had to connect one node from the first tree to another node in the second tree.
        Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.
        """

        N, M = len(edges1) + 1, len(edges2) + 1

        # Build adjacency list and find root for a tree
        def build_adj_list(edges, size):
            is_root = [True] * size
            adj = defaultdict(list)
            for src, trgt in edges:
                is_root[trgt] = False
                adj[src].append(trgt)
            # The root is the only node never targeted
            return adj, is_root.index(True)

        # BFS to determine parity (even/odd distance) from root for all nodes
        def even_steps_from_root(adj, size, root):
            res = [True] * size  # True for even, False for odd
            q = deque([root])
            is_even = True
            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    res[cur] = is_even
                    for nei in adj[cur]:
                        q.append(nei)
                is_even = not is_even
            return res

        # Build adjacency lists and find roots for both trees
        (adj1, root1), (adj2, root2) = build_adj_list(edges1, N), build_adj_list(
            edges2, M
        )
        # Get parity (even/odd) for all nodes in both trees
        even_from_root1, even_from_root2 = even_steps_from_root(
            adj1, N, root1
        ), even_steps_from_root(adj2, M, root2)
        # Count number of even nodes in tree2
        evens_from_root2 = even_from_root2.count(True)
        # The best you can do in tree2 is to connect to a node that maximizes the number of even or odd nodes
        max_targets2 = max(evens_from_root2, M - evens_from_root2)
        # Count number of even and odd nodes in tree1
        num_evens1 = even_from_root1.count(True)
        num_odds1 = N - num_evens1

        # For each node in tree1, if it's even, its targets are all even nodes in tree1 plus max_targets2 from tree2
        # If it's odd, its targets are all odd nodes in tree1 plus max_targets2 from tree2
        return [
            (
                num_evens1 + max_targets2
                if even_from_root1[i]
                else num_odds1 + max_targets2
            )
            for i in range(N)
        ]


# Time Complexity Analysis:
# Let n = number of nodes in tree1, m = number of nodes in tree2.
# - build_adj_list: O(n) and O(m) for each tree.
# - even_steps_from_root: O(n) and O(m) for each tree (BFS visits each node once).
# - Counting evens/odds: O(n) and O(m).
# - Final list comprehension: O(n).
# Total: O(n + m), which is efficient for n, m <= 1e5.

# Example 1:
# Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
# Output: [8,7,7,8,8]
