# Number: 3312
# Title: Sorted GCD Pair Queries
# Difficulty: Hard
# Tags: Array, Hash Table, Math, Binary Search, Combinatorics, Counting, Number Theory, Prefix Sum
# Language: Python3
# URL: https://leetcode.com/problems/sorted-gcd-pair-queries/
# Date: 2026-07-18
# Runtime: 0391ms (Beats 100%)
# Memory: N/A


MX = 5 * (10 ** 4)
comp = bytearray(MX + 1)
for p in range(2, isqrt(MX) + 1):
    if not comp[p]:
        comp[p * p :: p] = b'\x01' * ((MX - p * p) // p + 1)
PRIMES = [p for p in range(2, MX + 1) if not comp[p]]

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        freq = [0] * (mx + 1)
        for v in nums:
            freq[v] += 1

        for p in PRIMES:
            if p > mx: break
            for i in range(mx // p, 0, -1):
                freq[i] += freq[i * p]

        g = [c * (c - 1) // 2 for c in freq]   

        for p in PRIMES:  
            if p > mx: break
            for i in range(1, mx // p + 1):
                g[i] -= g[i * p]

        s = list(accumulate(g))
        return [bisect_right(s, q) for q in queries]