from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        """
        Problem: Count Subarrays of Length Three With a Condition; leetcode #3392
        Given an integer array nums, return the number of subarrays of length 3 such that
        the sum of the first and third numbers equals exactly half of the second number.

        Example 1:
        Input: nums = [1,2,1,4,1]
        Output: 1
        Explanation: Only the subarray [1,4,1] satisfies the condition.

        Example 2:
        Input: nums = [1,1,1]
        Output: 0
        Explanation: [1,1,1] does not satisfy the condition.

        Constraints:
        - 3 <= nums.length <= 100
        - -100 <= nums[i] <= 100
        """
        return sum(
            1
            for i in range(1, len(nums) - 1)
            if 2 * (nums[i - 1] + nums[i + 1]) == nums[i]
        )


# Intuitive (slower) approach:
#     res = 0
#     for i in range(1, len(nums) - 1):
#         if 2 * (nums[i - 1] + nums[i + 1]) == nums[i]:
#             res += 1
#     return res
