""" 40. Combination Sum II

Question:

    Given a collection of candidate numbers and a target number, find all unique
    combinations in candidates where the candidate numbers sums to target.

"""

class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()

        def backtrack(start, path, pathSum):
            if pathSum < 0:
                return
            if pathSum == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] <= pathSum:
                    backtrack(start, path + [candidates[i]], pathSum -
                            candidates[i])

        backtrack(0, [], target)
        return result
