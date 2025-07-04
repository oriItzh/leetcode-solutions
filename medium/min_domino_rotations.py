from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        Problem: Minimum Domino Rotations For Equal Row; leetcode #1007
        In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino.
        (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

        We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

        Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

        If it cannot be done, return -1.
        """
        candidates = [tops[0], bottoms[0]]
        n = len(tops)
        res = -1
        for candidate in candidates:
            if any(bottom != candidate and top != candidate for bottom, top in zip(tops, bottoms)):
                continue
            swapsT = n - sum(1 for tile in tops if tile == candidate)
            swapsB = n - sum(1 for tile in bottoms if tile == candidate)
            minSwaps = min(swapsT, swapsB)
            res = minSwaps if res == -1 else min(res, minSwaps)

        return res
