# 13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and
M.

Given a roman numeral, convert it to an integer.

---

We can decode the roman numeral into an integer by examining every pair of the
symbols to check for the conditions where I comes before V, X or X comes before
L or C and C comes before D and M. These form edge cases where we should
decrement by the first symbol.

This would be O(n) in time complexity.

---

Python:

```python

class Solution13:

    def romanToInt(self, s):

        m = {
            "I" : 1, "V" : 5", "X" : 10,
            "L" : 50, "C" : 100,
            "D" : 500, "M" : 1000
        }

        i, result = 0, 0

        while i < len(s):
            
            if i == len(s) - 1:
                result += m[s[i]]

            elif (s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X")) or \
                (s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C")) or \
                (s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M")):
                result += m[s[i+1]] - m[s[i]]
                i += 1

            else:
                result += m[s[i]]

            i += 1

        return result
```
