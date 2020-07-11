""" 78. Subsets

Question:

    Given a set of distinct integers, nums, return all possible subsets (the
    power set). The solution set must not contain duplicate subsets.

+++

Solution:

    The subset of sets are built upon each other. We repeat the process of
    taking out the set from the result, then add the element as a new set, as
    well as adding the element to the existing sets.

"""

class Solution:
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            temp = result.copy()
            for subset in temp:
                temp.append(subset + [num])
            result = temp
        return result

