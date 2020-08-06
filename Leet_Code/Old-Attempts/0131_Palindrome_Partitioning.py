""" 131. Palindrome Partitioning

Question:

    Given a string s, partition s such that every substring of the partition is
    a palindrome.

    Return all possible palindrome partitioning of s.

+++

Solution:

    We can use backtracking algorithm to explore all different possible
    partitioning and substring by checking whether it is a palindrome at each
    step.

"""

class Solution:
    def partition(self, s):
        result = []

        def backtrack(start, path):
            if start == len(s):
                result.append(path)
                return
            for i in range(start, len(s)):
                curr = [start:i+1]
                if curr == curr [::-1]:
                    backtrack(i+1, path + [curr])

        backtrack(0, [])
        return result
