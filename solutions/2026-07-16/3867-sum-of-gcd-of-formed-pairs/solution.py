# Number: 3867
# Title: Sum of GCD of Formed Pairs
# Difficulty: Medium
# Tags: Array, Math, Two Pointers, Sorting, Simulation, Number Theory
# Language: Python3
# URL: https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/
# Date: 2026-07-16
# Runtime: 71ms (Beats 73.12%)
# Memory: N/A

from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        gcdprefix = []
        mx = -1
        for i in nums:
            mx = max(mx, i)
            gcdprefix.append(gcd(i,mx))
        gcdprefix.sort()
        totalgcd = 0
        for i in range(len(gcdprefix)//2):
            totalgcd += gcd(gcdprefix[i], gcdprefix[-(i+1)])
        return totalgcd