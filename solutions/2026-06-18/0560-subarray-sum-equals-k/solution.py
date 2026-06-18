# Number: 0560
# Title: Subarray Sum Equals K
# Difficulty: Medium
# Tags: Array, Hash Table, Prefix Sum
# Language: Python3
# URL: https://leetcode.com/problems/subarray-sum-equals-k/
# Date: 2026-06-18
# Runtime: 31ms (Beats 77.66%)
# Memory: 21.74MB (Beats 77.66%)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0 
        curr_sum = 0 

        count_map  = {0:1}

        for num in nums:
            curr_sum = num + curr_sum
            target = curr_sum - k
            if target in count_map:
                count +=  count_map[target]
            if curr_sum in count_map:
                count_map[curr_sum] += 1
            else:
                count_map[curr_sum] = 1
        return count


