# 13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and
M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added
together. 12 is written as XII, which is simply X + II. The number 27 is
written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written
as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six
instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

---

This is a simple case of creating a symbol to value mapping; then examine the
characters for every pair to check for 6 cases where subtraction must occur.

---

Python:

```python

class Solution13:

    def __init__(self):
        self.m = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

    def romanToInt(self, s):

        i, result = 0, 0

        while i < len(s):

            if i == len(s) - 1:
                result += self.m[s[i]]
            elif (s[i+1] == "V" or s[i+1] == "X") and s[i] == "I":
                result += self.m[s[i+1]] - 1
                i += 1
            elif (s[i+1] == "L" or s[i+1] == "C") and s[i] == "X":
                result += self.m[s[i+1]] - 10
                i += 1
            elif (s[i+1] == "D" or s[i+1] == "M") and s[i] == "C":
                result += self.m[s[i+1]] - 100
                i += 1
            else:
                result += self.m[s[i]]
            i += 1

        return result
```

