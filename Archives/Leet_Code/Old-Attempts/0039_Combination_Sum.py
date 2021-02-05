""" 39. Combination Sum

Question:

    Given a set of candidate numbers and a target number, find all unique
    combinations in candidates where the candidate numbers sums to target.

"""

class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, path, pathSum):
            if pathSum < 0:
                return
            if pathSum == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                if candidates[i] <= pathSum:
                    backtrack(i, path + [candidates[i]], pathSum - candidates[i])

        backtrack(candidates, [], target)
        return result
