# Number: 0004
# Title: Median of Two Sorted Arrays
# Difficulty: Hard
# Tags: Array, Binary Search, Divide and Conquer
# Language: Python3
# URL: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Date: 2026-06-19
# Runtime: 2ms (Beats 100%)
# Memory: N/A

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)

        n = len(merged)
        mid = n // 2

        if n % 2 == 1:
            return merged[mid]
        else:
            return (merged[mid - 1] + merged[mid]) / 2
