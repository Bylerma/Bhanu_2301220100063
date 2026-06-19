# Number: 0088
# Title: Merge Sorted Array
# Difficulty: Easy
# Tags: Array, Two Pointers, Sorting
# Language: Python3
# URL: https://leetcode.com/problems/merge-sorted-array/
# Date: 2026-06-19
# Runtime: 0 ms (Beats 100%)
# Memory: N/A

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """     
        for i in range(0,n):
            nums1[m+i] = nums2[i]
        
        nums1.sort()

        
    
        