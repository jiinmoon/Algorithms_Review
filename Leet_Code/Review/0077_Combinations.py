""" 77. Combinations

Question:

    Given two integers n and k, return all possible combinations of k numbers
    out of 1 to n.

+++

Solution:

    We may use a backtrack algorithm to explore all paths down to build the
    combinations. 

"""

class Solution:
    def combine(self, n, k):
        result = []

        def backtrack(start, path):
            if len(path) == k:
                result.append(path)
            for i in range(start, n+1):
                backtrack(i+1, path + [i])

        backtrack(1, [])
        return result


