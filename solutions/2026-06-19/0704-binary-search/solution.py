# Number: 0704
# Title: Binary Search
# Difficulty: Easy
# Tags: Array, Binary Search
# Language: Python3
# URL: https://leetcode.com/problems/binary-search/
# Date: 2026-06-19
# Runtime: 0 ms (Beats 100%)
# Memory: 2MB (Beats 100%)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1
