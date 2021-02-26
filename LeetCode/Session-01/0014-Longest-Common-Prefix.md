# 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string "".

---

Naive approach would be to compare every string against each other to find the
longest prefix.

Better method would be actually simply the sort the given array of strings
alphabetical order. Hence, if there exists a common prefix, then all we need to
compare is the shortest length string (first) and the longest length string
(last). This would be O(n * log(n)) in time complexity.

---

Python: Sort first approach.

```python

class Solution14:

    def longestCommonPrefix(self, strs):

        if not strs:
            return ""

        strs.sort()
        first, last = strs[0], strs[-1]

        i = 0
        while i < len(first) and first[i] == last[i]:
            i += 1

        return first[:i]
```
