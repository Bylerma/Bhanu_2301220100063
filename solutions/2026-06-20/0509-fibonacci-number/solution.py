# Number: 0509
# Title: Fibonacci Number
# Difficulty: Easy
# Tags: Math, Dynamic Programming, Recursion, Memoization
# Language: Python3
# URL: https://leetcode.com/problems/fibonacci-number/
# Date: 2026-06-20
# Runtime: 0 ms (Beats 100%)
# Memory: N/A

class Solution:
    def fib(self, n):

        ft, st = 0, 1

        for _ in range(1, n + 1):
            tt = ft + st
            ft = st
            st = tt

        return ft