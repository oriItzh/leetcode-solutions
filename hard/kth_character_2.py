"""
LeetCode 3307: Find the K-th Character in String Game II

This solution uses a binary tree approach to efficiently find the k-th character
without simulating the entire string construction process.

Key insights:
1. Each operation doubles the string length, creating a binary tree structure
2. We can trace back from position k to find which operations affect it
3. Operations of type 1 increment characters, type 0 keep them unchanged
4. The algorithm works in O(log k) time instead of O(k) simulation
"""

from typing import List


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        """
        3307. Find the K-th Character in String Game II

        Alice and Bob are playing a game. Initially, Alice has a string word = "a".

        You are given a positive integer k. You are also given an integer array operations, 
        where operations[i] represents the type of the ith operation.

        Now Bob will ask Alice to perform all operations in sequence:

        If operations[i] == 0, append a copy of word to itself.
        If operations[i] == 1, generate a new string by changing each character in word to 
        its next character in the English alphabet, and append it to the original word. 
        For example, performing the operation on "c" generates "cd" and performing the 
        operation on "zb" generates "zbac".
        
        Return the value of the kth character in word after performing all the operations.

        Note that the character 'z' can be changed to 'a' in the second type of operation.

        ALGORITHM APPROACH:
        Instead of simulating the string construction (which would be too slow for k up to 10^14),
        we use a binary tree approach. Each operation doubles the string length, creating a 
        binary tree structure where:
        - The string length after n operations is 2^n
        - Position k maps to a path in this binary tree
        - We trace back from position k to find which operations affect it
        - Operations of type 1 increment the character, type 0 keep it unchanged

        Time Complexity: O(log k + operations.length)
        Space Complexity: O(1)

        Example 1:
        Input: k = 5, operations = [0,0,0]
        Output: "a"

        Explanation:
        Initially, word == "a". Alice performs the three operations as follows:
        Appends "a" to "a", word becomes "aa".
        Appends "aa" to "aa", word becomes "aaaa".
        Appends "aaaa" to "aaaa", word becomes "aaaaaaaa".
        
        Example 2:
        Input: k = 10, operations = [0,1,0,1]
        Output: "b"

        Explanation:
        Initially, word == "a". Alice performs the four operations as follows:
        Appends "a" to "a", word becomes "aa".
        Appends "bb" to "aa", word becomes "aabb".
        Appends "aabb" to "aabb", word becomes "aabbaabb".
        Appends "bbccbbcc" to "aabbaabb", word becomes "aabbaabbbbccbbcc".

        Constraints:
        1 <= k <= 10^14
        1 <= operations.length <= 100
        operations[i] is either 0 or 1.
        The input is generated such that word has at least k characters after all operations.
        """

        def get_operation_for_position(position: int) -> int:
            """
            Get the operation type that determines the character at a given position.
            
            The string grows in a binary tree pattern, where each operation doubles
            the string length. We use bit operations to find which operation level
            this position belongs to.
            
            Args:
                position: 1-indexed position in the final string
                
            Returns:
                The operation type (0 or 1) that affects this position
            """
            operation_level = (position - 1).bit_length() - 1
            return operations[operation_level]

        # Track the cumulative character shift from all transformations
        character_shift = 0
        current_position = k
        
        # Work backwards through the binary tree structure to find transformations
        while current_position > 1:
            # Get the operation that affects this position
            operation_type = get_operation_for_position(current_position)
            
            # Find the most significant bit position (operation level)
            msb_position = current_position.bit_length() - 1
            
            # Check if current position is a power of 2 (start of a new level)
            if current_position > 0 and (current_position - 1) & current_position == 0:
                # At power of 2 positions, we need to account for all previous operations
                character_shift += sum(operations[:msb_position])
            else:
                # For other positions, only the current operation affects the shift
                character_shift += operation_type
            
            # Move to the corresponding position in the previous level
            # by removing the most significant bit
            current_position ^= 1 << msb_position

        # Convert the accumulated shift to the final character
        # Using modulo 26 to handle wrapping from 'z' to 'a'
        final_character = chr(ord("a") + character_shift % 26)
        return final_character
