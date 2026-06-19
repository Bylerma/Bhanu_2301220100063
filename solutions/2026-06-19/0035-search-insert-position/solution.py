# Number: 0035
# Title: Search Insert Position
# Difficulty: Easy
# Tags: Array, Binary Search
# Language: Python3
# URL: https://leetcode.com/problems/search-insert-position/
# Date: 2026-06-19
# Runtime: 0ms (Beats 100%)
# Memory: 19.86MB (Beats 100%)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        
        return low
