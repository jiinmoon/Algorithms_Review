""" 40. Combination Sum II

Question:

    Same as question 39, however, there will be duplicate elements present.
    Find all unique set of combinations.

+++

Solution:

    In order to avoid selecting the duplicate elements in a row, we will first
    sort the given array, and then screen out the duplicates as we select our
    candidates for next depth.

"""

class Solution:
    def combination_sum_2(self, cnadidates, target):
        m = len(candidates)
        result = []
        candidates.sort()

        def backtrack(start, path, pathSum):
            if pathSum < 0:
                return
            if pathSum == 0:
                result.append(path)
                return
            for i in range(start, m):
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                backtrack(i+1, path + [candidates[i]], pathSum - candidates[i])
        
        backtrack(0, [], target)
        return result
