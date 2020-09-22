1153 String Transforms Into Another String
==========================================

Given two strings str1 and str2 of the same length, determine whether you can
transform str1 into str2 by doing zero or more conversions.

In a single conversion, you can convert all occurrences of one char in str1 to
any other lowercase English character.

---

In essence, the question is about whether every character in the str1 can be
mapped to str2 without overlapping.

First, we can check whether the conversion is possible by checking whether
every character in the alphabet is present within the str2 - and if str1 and
str2 is not same to begin with, then it is impossible to convert as all the
characters are used up and mapping any one in str1 will simply mapped to
another that is already used in the str2.

Next, we record the all indicies of each character appearing in the str1. Then,
for each appearing character in str1, we check its indicies against the str2.
Since all indicies in str1 comes from a single character, it should also be
true that all characters in the str2 at these indices should be same as well.
If not, then doing a conversion means that it will be mapped to two different
positions; impossible to transform.

The time complexity should be O(n).

---

Python:

```python:
class Solution:
    def canConvert(self, str1, str2):
        if str1 == str2:
            return True
        if len(set(str2)) == 26:
            return False
        
        charToIndicies = collections.defaultdict(int)
        for i, c in enumerate(str1):
            charToIndicies[c].append(i)

        for _, indicies in charToIndicies.items():
            if len(set(str2[i] for i in indicies)) != 1:
                return False

        return True
```
