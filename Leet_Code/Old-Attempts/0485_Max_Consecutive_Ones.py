""" 485. Max Consecutive Ones

Question:

    Given a binary array, find the max consecutive ones.

+++

Solution:

    Trivial algorithm - iterate and count; reset when the num encountered is 0.
    Linear time complexity as it is unavoidable to visit and examine each of the
    elements.

"""

class Solution:
    def maxConsecutiveOnes(self, nums):
        currCount = 0
        maxCount = 0
        for num in nums:
            if num:
                currCount += 1
            else:
                currCount = 0
            maxCount = max(maxCount, currCount)
        return maxCount
