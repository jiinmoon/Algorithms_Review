""" 5.3 Flip Bit To Win


Question:

    You have an integer and you can flip exactly one bit from a 0 to a 1. Write
    a code to find the length of the longest sequence of 1s you could create.

Example:

    Input:  1775 -> (11011101111)
    OUtput: 8

---

Treat this problem as a finding max problem. As we go through the sequence of 1s
and 0s, we consider each length (noted by the 0). If the sum of prev/and curr
sequences lengths are greater than the maxLength, then update the maxLength.

"""
