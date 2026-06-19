# Number: 0033
# Title: Search in Rotated Sorted Array
# Difficulty: Medium
# Tags: Array, Binary Search
# Language: Python3
# URL: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Date: 2026-06-19
# Runtime: 20260ms (Beats 100%)
# Memory: N/A

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:

                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else:

                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1