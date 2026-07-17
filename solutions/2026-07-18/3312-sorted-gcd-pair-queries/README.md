# 3312. Sorted GCD Pair Queries

![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red) ![Tag: Array](https://img.shields.io/badge/Tag-Array-blue) ![Tag: Hash Table](https://img.shields.io/badge/Tag-Hash%20Table-blue) ![Tag: Math](https://img.shields.io/badge/Tag-Math-blue) ![Tag: Binary Search](https://img.shields.io/badge/Tag-Binary%20Search-blue) ![Tag: Combinatorics](https://img.shields.io/badge/Tag-Combinatorics-blue) ![Tag: Counting](https://img.shields.io/badge/Tag-Counting-blue) ![Tag: Number Theory](https://img.shields.io/badge/Tag-Number%20Theory-blue) ![Tag: Prefix Sum](https://img.shields.io/badge/Tag-Prefix%20Sum-blue)

## 🔗 Link
[LeetCode Problem URL](https://leetcode.com/problems/sorted-gcd-pair-queries/)

## 📝 Problem Description
You are given an integer array nums of length n and an integer array queries.

Let gcdPairs denote an array obtained by calculating the GCD of all possible pairs (nums[i], nums[j]), where 0 <= i < j < n, and then sorting these values in ascending order.

For each query queries[i], you need to find the element at index queries[i] in gcdPairs.

Return an integer array answer, where answer[i] is the value at gcdPairs[queries[i]] for each query.

The term gcd(a, b) denotes the greatest common divisor of a and b.

 
Example 1:


Input: nums = [2,3,4], queries = [0,2,2]

Output: [1,2,2]

Explanation:

gcdPairs = [gcd(nums[0], nums[1]), gcd(nums[0], nums[2]), gcd(nums[1], nums[2])] = [1, 2, 1].

After sorting in ascending order, gcdPairs = [1, 1, 2].

So, the answer is [gcdPairs[queries[0]], gcdPairs[queries[1]], gcdPairs[queries[2]]] = [1, 2, 2].


Example 2:


Input: nums = [4,4,2,1], queries = [5,3,1,0]

Output: [4,2,1,1]

Explanation:

gcdPairs sorted in ascending order is [1, 1, 1, 2, 2, 4].


Example 3:


Input: nums = [2,2], queries = [0,0]

Output: [2,2]

Explanation:

gcdPairs = [2].


 
Constraints:


	2 <= n == nums.length <= 105
	1 <= nums[i] <= 5 * 104
	1 <= queries.length <= 105
	0 <= queries[i] < n * (n - 1) / 2

## 💡 Approach & Notes
<!-- Describe your approach, notes, and complexity here (e.g., O(n) time, O(1) space) -->

## 📊 Submission Stats
| Language | Runtime | Memory | Date |
| --- | --- | --- | --- |
| Python3 | 0391ms (Beats 100%) | N/A | 2026-07-18 |
