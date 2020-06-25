""" 5.1 Insertion

Question:

    You are given two 32-bit numbers, N and M, and two bit positions, i and j.
    Write a method to insert M into N such that M starts at bit j and ends at
    bit i. You can assume that the bits j through i have enough space to fit all
    of M. Thatis, if M = 10011, you can assume that there are at least 5 bits
    between j and i. You would not, for example, have j = 3 and i = 2, because M
    could not fully fit between bit 3 and bit 2.

Example:

    Input:

        N   =   1000 0000 000
        M   =   10011
        i = 2, j = 6

    Output:
        N   =   1000 1001 100

---

The given indicies are 0 index'd.

To perform this bit manipulation, we need to do following:

    1. clear the N from bit i to j to prepare for OR operation with M
    2. shift M to the left by i
    3. merge N and M by OR-operation

"""

class Solution:
    def insertion(self, n, m, i, j):
        """ insert m into n at index i through j """

        # 1. prepare a mask
        left = -1 << (j + 1)
        right = (1 << i) - 1 # quite smart operation
        mask = left | right

        # 2. clear N betwen index i and j with mask
        n = n & mask

        # 3. shift M to left by i
        m = m << i

        # 4. merge N and M
        return n | m

