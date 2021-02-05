# 1153. String Transformation Into Another String

Given two strings str1 and str2 of the same length, determine whether you can
transform str1 into str2 by doing zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to
any other lowercase English character.

Return true if and only if you can transform str1 into str2.

---

The problem is essentially a mapping problem where we map each of the character
from one string onto another.

So, we first iterate on the first string to create a mapping between its
character to index. Note that some characters will appear at many different
indicies. Then, we iterate on this created mapping to to check to see that
mapping from one string to another is possible by checking to see that the
there should only be a single character as we map all the indicies from string
1 to another.

---

Python:

```python

class Solution:
    def canConvert(self, str1, str2):
        # all possible character mapping has been taken
        if len(set(str2)) == 26 and str1 != str2:
            return False

        charToIndicies = collections.defaultdict(list)
        for i, char in enumerate(str1):
            charToIndicies[char].append(i)

        for char, indicies in charToIndicies.items():
            if len(set(str2[i] for i in indicies)) != 1:
                return False

        return True
```
