""" 47. Permutations II

Question:

    Given a collection of numbers that might contain duplicates, return all
    possbile unique permutations.

+++

Solution:

    Same backtracking algorithm - but we sort the given list beforehand to avoid
    selecting the duplicate.

"""

class Solution:
    def permuteUnique(self, nums):
        result = []
        nums.sort()

        def backtrack(nums, path):
            if not nums:
                result.append(path)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]])

        backtrack(nums, [])
        return result
