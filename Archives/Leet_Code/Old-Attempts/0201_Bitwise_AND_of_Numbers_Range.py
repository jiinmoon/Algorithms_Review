""" 201. Bitwise AND of Numbers Range

Question:

    Given a range [m, n] where 0 <= m <= n <= 2 ** 31 - 1, return the bitwise
    AND of all numbers in this range, inclusive.

+++

Solution:

    The naive solution would be to attempt to simply perform bitwise AND
    operations with all numbers in range.

    However, because of m <= n, there is a bit index where the bits of m and n
    would be same. This is easily seen with examples.

    Suppose m = 3, n = 9.

    m = 0000 0011
    n = 0000 1001

    Like this, if there isn't? AND operation would simply result in 0 - and all
    subsequent results would also remain 0. Thus, this would be one early exit
    strategy to add to our naive solution.

    But when we iterate bit by bit, and if we find the point where m == n, then
    this has to remain.

    Suppose m = 8, n = 11.

    m   = 0000 1000
    9   = 0000 1001
    10  = 0000 1010
    n   = 0000 1011

    The 1 on the 4th index is same; and notice that as we increment by 1, the
    bits turn off/on at alternate places - meaning that with AND operation, they
    will simply result in 0. However, this process stops until we reach that 4th
    index.

    Hence, our algorithm is as follows; until m == n, we rightshift m and n.
    Then, when they are equal, we can simply return the leftover bit from either
    m or n leftshifted by the original amount with shifted to right.

"""

class Solution:
    def rangeBitwiseAnd(self, m, n):
        shiftCount = 0
        while m != n:
            m >>= 1
            n >>= 1
            if not m or not n:
                return 0
            shiftCount += 1
        return m <<= shiftCount
