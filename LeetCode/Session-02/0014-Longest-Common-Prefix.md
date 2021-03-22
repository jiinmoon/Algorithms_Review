# 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string "".

---

Naive approach to the problem would be to consider every string and build our
prefix forward while comparing from each string's prefix.

However, we can avoid having to explore all strings by first sorting the given
array of strings by its length and alphanumerical orders. Hence, shortest,
ordered string comes first and longest, ordered string comes last. By doing so,
we can conclude that if there exists a prefix, its length must be less than the
first string in this sorted list and prefix should be shared by first and last
string.

So, time complexity would be reduced to simply sorting the entire array of
strings which is O(n * log(n)).

---

Python:

```python

class Solution14:

    def longestCommonPrefix(self, strs):

        if not strs:
            return ""
        if len(strs) < 2:
            return strs[0]

        strs.sort()

        first, last = strs[0], strs[-1]
        i = 0
        while i < len(first) and first[i] == last[i]:
            i += 1

        return first[:i]
```
