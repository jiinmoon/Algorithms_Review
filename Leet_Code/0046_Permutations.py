""" 46. Permutations

Question:

    Given a collection of distinct integers, return all possible permutations.

"""

class Solution:
    def permute(self, nums):
        result = []

        def backtrack(nums, path):
            if not nums:
                result.append(path)
                return
            for i in range(nums):
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]])

        backtrack(nums, [])
        return result
