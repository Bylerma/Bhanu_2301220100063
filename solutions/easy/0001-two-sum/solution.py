# Number: 0001
# Title: Two Sum
# Difficulty: Easy
# Tags: Array, Hash Table
# Language: Python3
# URL: https://leetcode.com/problems/two-sum/
# Date: 2026-06-17
# Runtime: 0ms (Beats 100%)
# Memory: 0.00MB (Beats 100%)

class Solution:
    def twoSum(self, nums, target):
        d = {}

        for i, x in enumerate(nums):
            need = target - x

            if need in d:
                return [d[need], i]

            d[x] = i
