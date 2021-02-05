# Compare Version Numbers

Compare two version numbers version1 and version2.

If version1 > version2 return 1,
If version1 < version2 return -1,
otherwise return 0.

You may assume that the version strings are non-empty and contain only digits
and the . character.

The . character does not represent a decimal point and is used to separate
number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is
the fifth second-level revision of the second first-level revision.

---

Split the given version numbers into int tokens about ".". If the length are
different, we fad smaller array with 0. Then, iterate on both while comparing
their values.

O(n + m) in time complexity.

---

Python:


```python

class Solution:

    def compareVersion(self, version1: str, version2: str) -> int:
        
        v1 = [int(v) for v in version1.split(".")]
        v2 = [int(v) for v in version2.split(".")]
        
        m = max(len(v1), len(v2))
        v1 += [0] * (m - len(v1))
        v2 += [0] * (m - len(v2))

        for a, b in zip(v1, v2):
            if a < b:
                return -1
            if a > b:
                return 1
        return 0

```
