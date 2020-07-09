""" 67. Add Binary

Question:

    Given two binary strings, return their sum in binary.

+++

Solution:

    Simplest solution is to utilize the lib.

"""

class Solution:
    def add_binary(self, a, b):
        a, b = int(a, 2), int(b, 2)
        return bin(a + b)[2:]
