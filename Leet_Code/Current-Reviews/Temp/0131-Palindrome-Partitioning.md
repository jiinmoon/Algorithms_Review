# 131. Plaindrome Partitioning

Given a string s, partition s such that every substring of the partition is
a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

---

Use recurisve backtracking to try to examine all prefixes of current string
segment; if prefix is determined to be a palindrome, it is added to our path
and traverse down until all string candidates are exhausted.

Time complexity is O(2^n) since we can potentially partition after each
characters - and we have to store these in call-stack so space is O(2^n) as
well.

---

Python:

```python

class Solution131:

    def partition(self, s: str) -> List[List[str]]:
        
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
