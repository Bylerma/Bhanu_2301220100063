# Number: 1752
# Title: Check if Array Is Sorted and Rotated
# Difficulty: Easy
# Tags: Array
# Language: Python3
# URL: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
# Date: 2026-06-18
# Runtime: 20260ms (Beats 100%)
# Memory: N/A

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        drops = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                drops += 1

        return drops <= 1