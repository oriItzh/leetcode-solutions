import heapq
from typing import List


class Solution:
    """
    Problem:
    There is a dungeon with n x m rooms arranged as a grid.

    You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes one second for one move and two seconds for the next, alternating between the two.

    Return the minimum time to reach the room (n - 1, m - 1).

    Two rooms are adjacent if they share a common wall, either horizontally or vertically.



    Example 1:

    Input: moveTime = [[0,4],[4,4]]

    Output: 7

    Explanation:

    The minimum time required is 7 seconds.

    At time t == 4, move from room (0, 0) to room (1, 0) in one second.
    At time t == 5, move from room (1, 0) to room (1, 1) in two seconds.
    Example 2:

    Input: moveTime = [[0,0,0,0],[0,0,0,0]]

    Output: 6

    Explanation:

    The minimum time required is 6 seconds.

    At time t == 0, move from room (0, 0) to room (1, 0) in one second.
    At time t == 1, move from room (1, 0) to room (1, 1) in two seconds.
    At time t == 3, move from room (1, 1) to room (1, 2) in one second.
    At time t == 4, move from room (1, 2) to room (1, 3) in two seconds.
    Example 3:

    Input: moveTime = [[0,1],[1,2]]

    Output: 4



    Constraints:

    2 <= n == moveTime.length <= 750
    2 <= m == moveTime[i].length <= 750
    0 <= moveTime[i][j] <= 109
    """

    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        """
        Problem: Minimum Time to Reach Last Room (LeetCode Contest)

        Approach: A* search algorithm with a custom heuristic
        - Use priority queue to explore paths with lowest estimated total time
        - Maintain a memoization table to avoid revisiting states with worse times
        - Use Manhattan distance-based heuristic to estimate remaining time

        Time Complexity: O(nm * log(nm)) where n,m are grid dimensions
        Space Complexity: O(nm) for memo table and heap
        """
        n, m = len(moveTime), len(moveTime[0])
        # Memoization table to store best time to reach each cell
        memo = [[-1] * m for _ in range(n)]
        memo[0][0] = 0
        heap = []

        # Calculate initial heuristic based on minimum possible steps to target
        min_steps = (n - 1) + (m - 1)  # Manhattan distance to target
        estimated_total = (min_steps * 3) // 2  # Average 1.5 seconds per move
        # Priority queue entry: (estimated_total_time, row, col, current_time)
        heapq.heappush(heap, (estimated_total, 0, 0, 0))

        # Possible movement directions (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            _, i, j, time = heapq.heappop(heap)
            # Found target cell
            if (i, j) == (n - 1, m - 1):
                return time

            # Calculate move cost: alternates between 1 and 2 based on total steps
            move_cost = 1 + ((i + j) & 1)  # Even sum = 1, Odd sum = 2

            # Explore all adjacent cells
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    # Must wait until moveTime allows entry
                    wait_time = max(time, moveTime[ni][nj])
                    new_time = wait_time + move_cost

                    # Update if we found a better path to this cell
                    if memo[ni][nj] == -1 or new_time < memo[ni][nj]:
                        memo[ni][nj] = new_time
                        # Calculate heuristic for remaining distance
                        remaining_steps = (n - 1 - ni) + (m - 1 - nj)
                        heuristic = (remaining_steps * 3) // 2
                        # Add to priority queue with updated estimate
                        heapq.heappush(heap, (new_time + heuristic, ni, nj, new_time))

        return memo[n - 1][m - 1]
