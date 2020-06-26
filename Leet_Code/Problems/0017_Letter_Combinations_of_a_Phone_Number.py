""" 17. Letter Combinations of a Phone Number

Question:

    Given a string containing digits from 2-9 inclusive, return all possible
    letter combinations that the number could represent.

"""

class Solution:
    def findLetterCombinations(self, digits):
        if not digits:
            return []

        letterMap = {
            '2' : 'abc', '3' : 'def', '4' : 'ghi',
            '5' : 'jkl', '6' : 'mno', '7' : 'pqrs',
            '8' : 'tuv', '9' : 'wxyz'
        }
        result = []

        def backtrack(s, path):
            if not s:
                result.append(path)
                return
            for char in letterMap[s[0]]:
                backtrack(s[1:], path + char)

        backtrack(digits, '')
        return result

