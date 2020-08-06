""" 70. Climbing Stairs

Question:

    You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can
    you climb to the top?

"""

from functools import lru_cache

class Solution:
    def climbStairs(self, n):
        @lru_cache(None)
        def climb(i):
            if i < 0:
                return 0
            if i == 0:
                return 1
            return climb(i-1) + climb(i-2)
        return climb(n)
