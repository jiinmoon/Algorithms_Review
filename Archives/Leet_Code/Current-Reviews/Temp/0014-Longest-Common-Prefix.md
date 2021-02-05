# 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string "".

---

#### (1) Brute Force.

We start from each of the characters in the beginning, and examine every string
to find the prefix. It will take upto O(n) where n is the length of all strings
combined.

#### (2) Sort first, then compare first and last.

By sorting the given string in lexicographical order, we can find the prefix
easily by comparing the first (smallest) to last (longest). O(n * log(n) + m)
time complxity where n is the number of strings and m is the length of shortest
string.

---

Python: sort.

```python

class Solution14:

    def longestCommonPrefix(self, strings):

        if not strings:
            return ""

        strings.sort()

        i = 0
        while i < len(strings[0]) and strings[0][i] == strings[-1][i]:
            i += 1

        return strings[0][:i]

```
