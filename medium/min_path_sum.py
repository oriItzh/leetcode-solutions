from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Problem: Min Path Sum; leetcode #64.
        Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
        which minimizes the sum of all numbers along its path.
        Note: You can only move either down or right at any point in time.

        Example 1:
        Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
        Output: 7
        Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
        Example 2:
        Input: grid = [[1,2,3],[4,5,6]]
        Output: 12

        Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 200
        0 <= grid[i][j] <= 200
        """
        # Dynamic Programming approach
        # We will iterate from the bottom-right corner to the top-left corner
        M, N = len(grid), len(grid[0])
        for i in reversed(range(M)):
            for j in reversed(range(N)):
                if i == M - 1 and j == N - 1:
                    continue
                right = grid[i][j + 1] if j + 1 < N else float("inf")
                down = grid[i + 1][j] if i + 1 < M else float("inf")
                grid[i][j] += min(right, down)
        return grid[0][0]
