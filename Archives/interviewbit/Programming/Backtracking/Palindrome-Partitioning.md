# Palindrome Partitioning

    Given a string s, partition s such that every string of the partition is
    a palindrome.

    Return all possible palindrome partitioning of s.

---

## Approach:

Use backtrack to try every substring segment; if segment is found to be
a palindrome, we add to path and recurse down to explore further.

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
                    ss = s[:i]
                    if ss == ss[::-1]:
                        helper(s[i:], path + [ss])
            
        result = []

        helper(s, [])

        return result

```
