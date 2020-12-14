# 13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and
M.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

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

We convert given roman numeral into integer by looking at every pair of
adjacent characters at a time. If pair can be evaluated to speical cases where
subtraction is used, we do so. This would be O(n) in time complexity.

---

Python:

```python

class Solution13:

    def __init__(self):
        this.m = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

    def romanToInteger(self, s):

        i, result = 0, 0

        while i < len(s):

            if i == len(s) - 1:
                result += this.m[s[i]]
            elif (s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X")) or \
                (s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C")) or \
                (s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M")):
                result += this.m[s[i+1]] - this.m[s[i]]
                i += 1
            else:
                result += this.m[s[i]]
            i += 1

        return result
```
