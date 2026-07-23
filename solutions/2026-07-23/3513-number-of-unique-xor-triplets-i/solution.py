# Number: 3513
# Title: Number of Unique XOR Triplets I
# Difficulty: Medium
# Tags: Array, Math, Bit Manipulation
# Language: Python3
# URL: https://leetcode.com/problems/number-of-unique-xor-triplets-i/
# Date: 2026-07-23
# Runtime: 0ms (Beats 100%)
# Memory: N/A

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        return 1 << n.bit_length()