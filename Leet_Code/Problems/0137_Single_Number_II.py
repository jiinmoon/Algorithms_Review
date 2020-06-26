""" 137. Single Number II

Question:

    Given a non-empty array of integers, every element appears three times
    except for one. Find that single one.

+++

Solution:

    [x1, x1, x1, ... , xn]

    3(x1 + x2 + ... + xn) + y

    To find that y, we assume that every element is appearing three times. Then,
    we can compute the hypothetical total by multiplying 3 to sum of single
    elements. But, our given array will be missing two from expected three of
    that single element. Thus, we can find the single one by taking the
    difference between our hypothetical sum - given sum // 2.

"""

class Solution:
    def singleNumber(self, nums):
        givenSum = sum(nums)
        hypotheticalSum = 3 * (set(nums))
        return (hypotheticalSum - givenSum) // 2
