# 17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

---

We can use backtracking algorithm to explore all possible letter combinations.
For every digit encountered, we add all possible letter that is mapped to the
digit to our current path that we are exploring. And then we recursively
explore until base case is reached where we have exhuasted all the digits to
explore; in which case, we append our path that have been built thus far to our
result.

---

Python: Backtracking approach.

```python

class Solution17:

    def __init__(self):
        self.digitMap = {
            "2" : "abc", "3" : "def", "4" : "ghi",
            "5" : "jkl", "6" : "mno", "7" : "pqrs",
            "8" : "tuv", "9" : "wxyz"
        }

    def letterCombinations(self, digits):
        
        def backtrack(digits, path):
            if not digits:
                result.append(path)
            else:
                # at each depth, take first digit and find all letter mapped
                # for each letter mapped, recursively explore down the new path
                for letter in self.digitMap(digits[0]):
                    backtrack(digits[1:], path + [letter])

        result = []
        backtrack(digits, [])

        return result
```
