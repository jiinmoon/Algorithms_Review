""" 70. Climbing Stairs

Question:

    You are climbing a stair case which takes n steps to reach top.

    Each time you can only take 1 or 2 steps. How many different ways can you
    reach to top?

+++

Solution:

    This is in fact a fib problem. The current answer depends upon the previous
    and prev of previous answers. The naive implementation of the fib problem
    in recursive way takes O(n!). To reduce this, we should utilize memoization
    technique, where we can store the answers of previous and look it up
    easily without having to compute again.

"""
from functools import lru_cache

class Solution:
    
    @lru_cache(None)
    def climb_stairs(self, n):
        if n <= 0:
            return 0
        if n <= 2:
            return 2
        return self.climb_stairs(n-1) + self.climb_stairs(n-2)

