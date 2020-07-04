""" 17. Letter Combinations of a Phone Number

Question:

    Given a string of digits, find all possible characters mappings based on
    the phone scheme (i.e. '2' is mapped to 'abc' and so on).

+++

Solution:

    We may approach this problem with the backtracking algorithm that will
    explore all combinations of our digits; and since these digits are mapped
    to multiple different characters, we should create a record to store these
    mappings and retrieve them as quick as possible - hashmap structure would
    suffice.

"""

class Solution:
    def letterCombinations(self, s):
        if not s:
            return []
        mappings = {
            '2' : 'abc', '3' : 'def', '4' : 'ghi',
            '5' : 'jkl', '6' : 'mno', '7' : 'pqrs',
            '8' : 'tuv', '9' : 'wxyz'
        }
        result = []

        def backtrack(digits, path):
            if not digits:
                result.append(path)
                return
            for char in mappings[digits[0]]:
                backtrack(digits[1:], path + char)

        backtrack(s, '')
        return result

