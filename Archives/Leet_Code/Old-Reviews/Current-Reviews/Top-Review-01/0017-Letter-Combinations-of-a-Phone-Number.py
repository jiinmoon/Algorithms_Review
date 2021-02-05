# 17 Letter Combinations of a Phone Number
#
# Prepare a hashmap where we have our digits mapped to the letters.
#
# Then, use backtracking algorithm to map each first digit to their
# corresponding letters.

class Solution:
    def letterCombinations(self, digits):
        digit_letters = {
            "2" : "abc", "3" : "def", "4" : "ghi",
            "5" : "jkl", "6" : "mno", "7" : "pqrs",
            "8" : "tuv", "9" : "wxyz"
        }

        def helper(digits, path):
            if not digits:
                res.append(path)
                return
            for letter in digit_letters[digits[0]]:
                helper(digits[1:], path + letter)

        res = list()
        helper(digits, "")
        return res
