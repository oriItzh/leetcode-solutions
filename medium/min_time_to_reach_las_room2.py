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
        n, m = len(moveTime), len(moveTime[0])
        memo = [[-1] * m for _ in range(n)]
        memo[0][0] = 0
        heap = []

        # Heuristic estimate: remaining steps * 1.5 (alternating 1/2 seconds)
        min_steps = (n - 1) + (m - 1)
        estimated_total = (min_steps * 3) // 2
        heapq.heappush(heap, (estimated_total, 0, 0, 0))  # (f = g + h, i, j, g)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            _, i, j, time = heapq.heappop(heap)
            if (i, j) == (n - 1, m - 1):
                return time

            move_cost = 1 + ((i + j) & 1)  # 1 if even, 2 if odd

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    wait_time = max(time, moveTime[ni][nj])
                    new_time = wait_time + move_cost

                    if memo[ni][nj] == -1 or new_time < memo[ni][nj]:
                        memo[ni][nj] = new_time
                        remaining_steps = (n - 1 - ni) + (m - 1 - nj)
                        heuristic = (remaining_steps * 3) // 2
                        heapq.heappush(heap, (new_time + heuristic, ni, nj, new_time))

        return memo[n - 1][m - 1]