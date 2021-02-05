# LeetCode Daily Challenge: August Week.1 - Day.4

## Question

Given a signed 32-bit integer, determine whether it is four of four.

## Solution

Naive solution would be to iteratively divide the given integer or start from
1 and compute all powers of fours to check whether the given integer is the
power of four. Since there are only so many powers of four within 32-bit
integer, this is not much of a compromise.

Improved solution would be just hardcode or precompute all the powers of four
values and check the given integer against it. Again, the limit of 32-bit means
that there can only be so many powers of four under 32-bit.

A constant time solution without extra space borrows the idea from the
determining the power of two. If a number is power of two, then it should only
have a single bit turned on. This can be checked with bit operation (n & (n-1)
== 0). Since the power of four is a subset of power of two, we need to check
for additional condition which is that all the bits where power of four
wouldn't have should be turned off. i.e. 0xAAAA AAAA in binary representation
has only the bits of power of two turned on while power of four is off.

Python:

```python
class Solution:
    def isPowerOfFour(self, n):
        return (n != 0) and (n & (n-1) == 0) and \
            (not n & 0xAAAAAAAA)
```

