""" 216. Combination Sum III

Question:

    Find all possible combinations of k numbers that add up to a number n, given
    that only numbers from 1 to 9 can be used and each combination should be a
    unique set of numbers.

+++

Solution:

    We use backtracking algorithm; at each iteration, we check for base case;
    then, whether our path has reached k numbers and sum to n. Else, we consider
    next recursive candidates from starting value to 10.

"""

class Solution:
    def combinationSumIII(self, k, n):
        result = []

        def backtrack(start, path):
            if len(path) > k or sum(path) > n:
                return
            if len(path) == k and sum(path) == n:
                result.append(path)
                return
            for num in range(start, 10):
                backtrack(num + 1, path + [num])

        backtrack(1, [])
        return result
