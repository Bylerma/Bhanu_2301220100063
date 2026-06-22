# 15. 3Sum

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange) ![Tag: Array](https://img.shields.io/badge/Tag-Array-blue) ![Tag: Two Pointers](https://img.shields.io/badge/Tag-Two%20Pointers-blue) ![Tag: Sorting](https://img.shields.io/badge/Tag-Sorting-blue)

## 🔗 Link
[LeetCode Problem URL](https://leetcode.com/problems/3sum/)

## 📝 Problem Description
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.


Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.


Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


 
Constraints:


	3 <= nums.length <= 3000
	-105 <= nums[i] <= 105

## 💡 Approach & Notes
<!-- Describe your approach, notes, and complexity here (e.g., O(n) time, O(1) space) -->

## 📊 Submission Stats
| Language | Runtime | Memory | Date |
| --- | --- | --- | --- |
| Python3 | 28ms (Beats 100%) | N/A | 2026-06-22 |
