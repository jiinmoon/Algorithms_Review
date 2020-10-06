# 1153 String Transforms Into Another String

Given two strings str1 and str2 of the same length, determine whether you can
transform str1 into str2 by doing zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to
any other lowercase English character.

Return true if and only if you can transform str1 into str2.

---

This is about the mapping one character from another. Thus, we can easily
screen out first by checking whether it would take more than 26 characters to
map to another string. Then, we create a hashmap of each character indicies
- then, the set of mapped indicies can be checked.

---

Python:

```python

class Solution:
    def canConvert(self, str1, str2):
        if str1 == str2: return True
        if len(set(str2)) == 26: return False

        charIndex = collections.defaultdict(list)
        for i, char in enumerate(str1):
            charIndex[char].append(i)

        for indicies in charIndex.values():
            if len(set(str2[i] for i in indicies)) != 1:
                return False

        return True
```
