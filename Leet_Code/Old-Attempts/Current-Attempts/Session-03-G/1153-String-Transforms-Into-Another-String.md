# 1153 String Transforms Into Another String

The problem is about mapping one char from another string onto another. This is
achieved with set data structure to find unique chars to mapped.

---

Python:

```python

class Solution:
    def stringTransforms(self, s, t):
        if s == t: return True
        if len(set(t)) == 26: return False

        charToIndex = dict()
        for i, char in enumerate(s):
            charToIndex[char] = i

        for indicies in charToIndex.values():
            if len(set(t[i] for i in indicies)) != 1:
                return False

        return True
```
