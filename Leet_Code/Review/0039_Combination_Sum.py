""" 39. Combination Sum

Question:

    Given a set of candidate numbers without duplicates, anda target number,
    find all unique combinations in candidates where the candidate numbers sums
    to target.

+++

Solution:

    Here, we utilize backtracking algorithm to explore all possible paths - and
    consider the pathSum. When the current path has reached the target, then we
    can add it to our result list to be returned.

"""

class Solution:
    def combination_sum(self, candidates, target):
        m = len(candidates)
        result = []

        def backtrack(start, path, pathSum):
            if pathSum < 0:
                return
            if pathSum == 0:
                result.append(path)
                return
            for i in range(start, m):
                if candidate < pathSum:
                    backtrack(i ,path + [candidates[i]], pathSum
                            - candidates[i])

        backtrack(0, [], target)
        return result

