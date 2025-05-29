from typing import List


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        """
        Problem: Total Characters in String After Transformations II; leetcode #3337

        You are given a string s consisting of lowercase English letters, an integer t representing the number of transformations to perform, and an array nums of size 26. In one transformation, every character in s is replaced according to the following rules:

        Replace s[i] with the next nums[s[i] - 'a'] consecutive characters in the alphabet. For example, if s[i] = 'a' and nums[0] = 3, the character 'a' transforms into the next 3 consecutive characters ahead of it, which results in "bcd".
        The transformation wraps around the alphabet if it exceeds 'z'. For example, if s[i] = 'y' and nums[24] = 3, the character 'y' transforms into the next 3 consecutive characters ahead of it, which results in "zab".
        Return the length of the resulting string after exactly t transformations.

        Since the answer may be very large, return it modulo 109 + 7.



        Example 1:

        Input: s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]

        Output: 7

        Explanation:

        First Transformation (t = 1):

        'a' becomes 'b' as nums[0] == 1
        'b' becomes 'c' as nums[1] == 1
        'c' becomes 'd' as nums[2] == 1
        'y' becomes 'z' as nums[24] == 1
        'y' becomes 'z' as nums[24] == 1
        String after the first transformation: "bcdzz"
        Second Transformation (t = 2):

        'b' becomes 'c' as nums[1] == 1
        'c' becomes 'd' as nums[2] == 1
        'd' becomes 'e' as nums[3] == 1
        'z' becomes 'ab' as nums[25] == 2
        'z' becomes 'ab' as nums[25] == 2
        String after the second transformation: "cdeabab"
        Final Length of the string: The string is "cdeabab", which has 7 characters.

        Example 2:

        Input: s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

        Output: 8

        Explanation:

        First Transformation (t = 1):

        'a' becomes 'bc' as nums[0] == 2
        'z' becomes 'ab' as nums[25] == 2
        'b' becomes 'cd' as nums[1] == 2
        'k' becomes 'lm' as nums[10] == 2
        String after the first transformation: "bcabcdlm"
        Final Length of the string: The string is "bcabcdlm", which has 8 characters.



        Constraints:

        1 <= s.length <= 105
        s consists only of lowercase English letters.
        1 <= t <= 109
        nums.length == 26
        1 <= nums[i] <= 25
        """

        MOD = 10**9 + 7

        # Initialize the matrix for the transformation
        def initialize_matrix():
            mat = [[0] * 26 for _ in range(26)]
            for src_letter, consec_len in enumerate(nums):
                for j in range(src_letter + 1, src_letter + consec_len + 1):
                    trgt_letter = j % 26
                    mat[trgt_letter][src_letter] += 1
            return mat

        def mat_mult(a, b):
            res = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for j in range(26):
                    for k in range(26):
                        res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % MOD
            return res

        def mat_pow(mat, power):
            result = [[int(i == j) for j in range(26)] for i in range(26)]
            while power:
                if power & 1:
                    result = mat_mult(result, mat)
                mat = mat_mult(mat, mat)
                power >>= 1
            return result

        def mat_vec_mult(mat, vec):
            res = [0] * 26
            for i in range(26):
                for j in range(26):
                    res[i] = (res[i] + mat[i][j] * vec[j]) % MOD
            return res

        # Initialize frequency vector
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord("a")] += 1

        mat = initialize_matrix()
        mat_t = mat_pow(mat, t)
        final_freq = mat_vec_mult(mat_t, freq)

        return sum(final_freq) % MOD
