""" 47. Permutations II

Question:

    Given a collections of numbers that may contain duplicates, return all
    possible unique permutations.

+++

Solution:

    Same backtracking approach; but we will sort and screen out the duplicates
    as we build our permutations.

"""

class Solution:
    def permute_unique(self, nums):
        result = []
        nums.sort()

        def backtrack(candidates, path):
            if not candidates:
                result.append(path)
                return
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1]:
                    continue
                backtrack(candidates[:i] + candidates[i+1:], path
                        + candidates[i]])

        backtrack(nums, [])
        return result

