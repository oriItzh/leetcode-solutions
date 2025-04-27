from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Problem: Two Sum (LeetCode #1)
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.

        Example 1:

        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
        Example 2:

        Input: nums = [3,2,4], target = 6
        Output: [1,2]
        Example 3:

        Input: nums = [3,3], target = 6
        Output: [0,1]
        

        Constraints:

        2 <= nums.length <= 104
        -109 <= nums[i] <= 109
        -109 <= target <= 109"""

        # Dictionary to store number -> index
        dict_nums = {}
        for i, num in enumerate(nums):
            to_find = target - num
            if to_find in dict_nums:
                return [dict_nums[to_find], i]
            dict_nums[num] = i
        return []

# Test case (only runs when script is executed directly)
if __name__ == "__main__":
    sol = Solution()
    result = sol.twoSum([2, 7, 11, 15], 9)
    print("Indices:", result)  # Expected: [0, 1]