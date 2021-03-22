# 17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

---

Here, we can use backtracking algorithm to generate all possible letter mapping
from each of the digits. At each depth of recursion, we find all letter mapping
for our current first digit. We continue to build our path down until we
consume all possible digits to explore.

---

Python:

```python

class Solution17:

    def letterCombinations(self, digits):

        m = {
            2 : "abc", 3 : "def", 4 : "ghi",
            5 : "jkl", 6 : "mno", 7 : "pqrs",
            8 : "tuv", 9 : " wxyz"
        }

        def backtrack(path, digits):
            
            if not digits:
                result.append(path)

            else:
                for letter in m[digits[0]]:
                    backtrack(path + [letter], digits[1:])

        result = []
        backtrack([], digits)

        return result
```

