""" 448. Find All Numbers Disappeared in an Array

Question:

    Given an array of integers where 1 <= a[i] <= n where n is the size of
    array, some elements appear twice and others appear once.

    Find all the elements of 1, n inclusive that do not appear in this array.

+++

Solution:

    We could sort the array to find the missing elements as we can find the
    duplicates easily in this case, and they won't match with their index.
    However, there is a linear time complexity algorithm which uses the array
    itself.

    The array has a property that its elements are bounded by its length, and
    that these have to appear at least once. Thus, we array index as a
    indication of whether the value that we have seen thus far appears or not.

    So, we first iterate to mark the elements appearing. This is done by
    using current element as a index - and mark that index by negation to avoid
    destroying the information. Then, the missing values can be found on second
    iteration where the indexes with positive values indicate that there was an
    duplicate at this position.

"""

class Solution:
    def findDisappearedNumbers(self, nums):
        m = len(nums)
        for i in range(m):
            pos = abs(nums[i]) - 1 # 0 indexed!
            nums[pos] = 0 - abs(nums[pos])
        result = [i + 1 for i in range(m) if nums[i] > 0]
        return result
