""" 46. Permutations

Question:

    Given a collectin of distinct integers, return all possible permutations.

+++

Solution:

    The back tracking algorithm can be used to generate all possible
    permutations.

"""

class Solution:
    def permute(self, nums):
        result = []

        def backtrack(candidates, path):
            if not candidates:
                result.append(path)
                return
            if i in range(len(candidates)):
                backtrack(candidates[:i] + candidates[i+1:], path
                        + candidates[i])

        backtrack(nums, [])
        return result

