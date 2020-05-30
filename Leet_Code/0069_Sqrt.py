""" 69. Sqrt

Question:

    Implement sqrt(int x).

+++

Solution:

    We can approach this problem as a math problem - solving it using namely
    Newton-Rhapson method. However, sqrt is basically a search number problem on
    the sorted number line. Meaning, we may apply the binary search algorithm.

"""

class Solution:
    def sqrt(self, x):
        if x < 2:
            return x
        lo, hi = 1, x
        while lo < hi:
            mid = lo + (hi - lo) // 2
            curr = mid * mid

            if curr == x:
                return mid
            elif curr > x:
                hi = mid
            else:
                lo = mid + 1
        return lo - 1
