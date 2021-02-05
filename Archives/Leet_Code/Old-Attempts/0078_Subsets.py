""" 78. Subsets

Question:

    Given a set of distinct integers, return all possible subsets.

"""

class Solution:
    def subsets(self, nums):
        result = [[]]

        for num in nums:
            temp = result.copy()
            for subset in temp:
                result.append(subset + [num])
            result = temp

        return result
