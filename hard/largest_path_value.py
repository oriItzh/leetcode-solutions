from collections import defaultdict, deque
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """
        Problem: Largest Color Value in a Directed Graph (LeetCode #1857)
        Approach: Topological Sort + Dynamic Programming
        - Build the graph and compute in-degrees for each node.
        - Use Kahn's algorithm for topological sorting.
        - For each node, maintain a count of the maximum number of each color along any path to that node.
        - If a cycle is detected (not all nodes are visited), return -1.
        
        Time Complexity: O(n + m), where n = number of nodes, m = number of edges
        Space Complexity: O(n * 26) for DP table (26 colors)
        """
        def _color(idx):
            # Convert color character to an integer index (0-25)
            return ord(colors[idx]) - ord('a')

        n = len(colors)
        adj = defaultdict(list)  # adjacency list for the graph
        in_deg = [0] * n         # in-degree for each node
        dp = [[0] * 26 for _ in range(n)]  # dp[i][c]: max count of color c to node i
        q = deque()              # queue for topological sort
        visited = 0              # count of visited nodes

        # Build the graph and compute in-degrees
        for src, trgt in edges:
            in_deg[trgt] += 1
            adj[src].append(trgt)

        # Initialize queue with nodes having zero in-degree
        for i in range(n):
            if in_deg[i] == 0:
                q.append(i)
            # Each node starts with its own color counted once
            dp[i][_color(i)] = 1
        
        # Topological sort and DP propagation
        while q:
            cur = q.popleft()
            visited += 1
            for nei in adj[cur]:
                for color in range(26):
                    # If the neighbor's color matches, increment count
                    maybe = 1 if color == _color(nei) else 0
                    # Update the DP table for the neighbor
                    dp[nei][color] = max(dp[nei][color], dp[cur][color] + maybe)
                in_deg[nei] -= 1
                # If in-degree becomes zero, add to queue
                if in_deg[nei] == 0:
                    q.append(nei)

        # If all nodes are visited, return the largest color value found
        # Otherwise, a cycle exists, return -1
        return max(max(row) for row in dp) if visited == n else -1
    
        # Time: O(n + m), Space: O(n * 26)
    

    # Example 1:



    # Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
    # Output: 3
    # Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
    # Example 2:



    # Input: colors = "a", edges = [[0,0]]
    # Output: -1
    # Explanation: There is a cycle from 0 to 0.
    

    # Constraints:

    # n == colors.length
    # m == edges.length
    # 1 <= n <= 105
    # 0 <= m <= 105
    # colors consists of lowercase English letters.
    # 0 <= aj, bj < n