# Letter Phone

    Given a digit string, return all possible letter combinations that the number
    could represent.

    The digit 0 maps to 0 itself.
    The digit 1 maps to 1 itself.

---

## Approach:

Prepare a digit to letter mapping; use backtrack to examine the first candidate
and map it to the letters to build the path. When we have exhuasted our
candidate pool, add finished path to our result.

---

Python:

```python

class Solution:

    letterMap = {
        "0" : "0",
        "1" : "1",
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"
    }

    def letterCombinations(self, A):

        def helper(candidates, path):

            if not candidates:
                result.append(path)

            else:
                for letter in Solution.letterMap[candidates[0]]:
                    helper(candidates[1:], path + letter)

        result = []

        helper(A, "")

        return result

```
