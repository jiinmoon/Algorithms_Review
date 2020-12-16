# Palindrome Partitioning

Given a string s, partition s such that every string of the partition is
a palindrome.

Return all possible palindrome partitioning of s.

---

We brute force backtrack to consider every possible substring; if we find
a substring that is a palindrome, we add to path and discover down the
recursion depth. When we exhaust all string, we can add our path to the result.

There are O(2^N) possible substrings generated and O(n) to check for
palindrome.

---

Python:

```python

class Solution:

    def palindromePartition(self, s):

        def helper(s, path):
            if not s:
                result.append(path)
            else:
                for i in range(1, len(s) + 1):
                    substr = s[:i]
                    if substr == substr[::-1]:
                        helper(s[i:], path + [substr])

        result = []

        helper(s, [])

        return result

```
