""" 169. Majority Element

Question:

    Given an array of size n, find the majority element. The majority element is
    the element that appears more than floor(n/2) times.

+++

Solution:

    I believe that we can apply majority voting algorithm here, but more simply,
    we can just count the elements.

"""

from collections import defaultdict

class Solution:
    def findMajorityElement(self, nums):
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if count[num] > len(nums) // 2:
                return num
        return -1
