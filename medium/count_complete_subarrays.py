from collections import defaultdict
from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        """
        Problem: Count Complete Subarrays in an Array ; leetcode #2799
        You are given an array nums consisting of positive integers.

        We call a subarray of an array complete if the following condition is satisfied:

        The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
        Return the number of complete subarrays.

        A subarray is a contiguous non-empty part of an array.

        

        Example 1:

        Input: nums = [1,3,1,2,2]
        Output: 4
        Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].
        Example 2:

        Input: nums = [5,5,5,5]
        Output: 10
        Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.
        

        Constraints:

        1 <= nums.length <= 1000
        1 <= nums[i] <= 2000"""
        n = len(nums)
        result = 0
        left = right = 0

        # Set of all distinct elements in the original array
        total_unique_elements = set(nums)

        # Dictionary to count elements in the current window
        window_count = defaultdict(int)

        while right < n:
            num = nums[right]
            window_count[num] += 1

            # Shrink the window from the left while it still contains all unique elements
            while len(window_count) == len(total_unique_elements):
                # All subarrays starting from 'left' to 'right' and ending at or after 'right' are valid
                result += n - right
                window_count[nums[left]] -= 1
                if window_count[nums[left]] == 0:
                    del window_count[nums[left]]
                left += 1

            right += 1

        return result
