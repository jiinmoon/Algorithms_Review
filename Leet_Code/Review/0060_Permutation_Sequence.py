""" 60. Permutation Sequence

Question:

    The set [1, 2, 3, ... , n] contains total of n! unique permutations.

    By listing and labeling all of the permutations in order, we get the
    following sequence for n = 3.

    1. [1, 2, 3]
    2. [1, 3, 2]
    3. [2, 1, 3]
    4. ...

    Given n and k, return the k-th permutation sequence.

+++

Solution:

    Naive approach would be to try and generate the permutations upto the k-th.
    However, there exists a solution that can solve this problem within
    a O(n^2) time, which leverages upon the fact that the permutations are
    ordered and has a predictable pattern.

    The trick is to find the each digit based on the ratio between k and the
    total number of possible permutation.

"""
from math import factorial

class Solution:
    def get_permutation(self, n, k):
        # prepare the sequences
        digits = [str(i) for i in range(1, n+1)]
        # possible permutations are n!
        permutations = factorial(n)
        k -= 1
        result = []

        while digits:
            # ratio of current digit
            digit = n * k // permutations
            result.append(digits[digit])
            del digits[digit]
            # update k and permutations to account for next iteration
            permutations //= n
            k -= digit * permutations
            n -= 1

        return ''.join(result)

