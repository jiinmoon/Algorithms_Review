""" 90. Subsets II

Question:

    Given a collection of integers that might contain duplicates, return all
    possible subsets. The solution set should not contain duplicate subsets.

"""

class Solution:
    def subsetsWithDup1(self, nums):
        # Backtracking approach.
        result = []
        nums.sort()

        def backtrack(start, path):
            # we do not have a goal; path that we are building is the each
            # subset that we should add to the result
            result.append(list(path))
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                backtrack(i+1, path +[nums[i]])

        backtrack(0, [])
        return result

    def subsetsWithDup2(self, nums):
        # Iterative method.
        result = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            temp = result.copy()
            for subset in temp:
                reslut.append(subset + nums[i])
        return result
