""" 179. Largest Number

Question:

    Given a list of non negative integers, arrange them such that they form the
    largest number.

+++

Solution:

    We can approach this problem simply by sorting the given list of integers
    using the custom key - where given two values a and b, we simply try to
    combine the two to see which one results in the higher value.

"""

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        customKey = lambda a, b: int(a + b) - int(b - a)
        nums = [ str(num) for num in nums ]
        sortedNums =
            list(
                sorted(
                    nums,
                    reverse = True,
                    key = cmp_to_key(customKey)))
        return '0' if sortedNums[0] == '0' else ''.join(sortedNums)

