# Number: 0035
# Title: Search Insert Position
# Difficulty: Easy
# Tags: Array, Binary Search
# Language: Python3
# URL: https://leetcode.com/problems/search-insert-position/
# Date: 2026-06-19
# Runtime: N/A
# Memory: N/A

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
