# 46 Permutations
#
# Utilize the backtracking algorithm to consider inserting the new element into
# the existing sets repeatedly.

class Solution:
    def permutations(self, nums):
        def helper(candidates, path):
            if not candidates:
                res.append(path)
                return
            for i in range(len(candidates)):
                helper(candidates[:i] + candidates[i+1:], path + [candidates[i]])

        res = list()
        helper(nums, list())
        return res

