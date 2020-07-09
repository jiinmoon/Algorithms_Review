""" 69. Sqrt(x)

Question:

    Implement int sqrt(int x) where x >= 0.

+++

Solution:

    Naive approach may try to repeatedly take each num upto sqrt of x. However,
    we can see this problem as a binary search problem on the number line. We
    know that value of x lies within the number line - and we are selecting
    value that can determine whether our current selection is too great or too
    low.

"""

class Solution:
    def my_sqrt(self, x):
        if x < 2:
            return x
        lo, hi = 0, x
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                hi = mid
            else:
                lo = mid + 1
        return lo - 1

