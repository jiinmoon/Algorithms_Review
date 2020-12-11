# 28. Implement strStr

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question
to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty
string. This is consistent to C's strstr() and Java's indexOf().

---

There are many efficient searching for needle in a haystack such as KMP or
Boyer-Mooer's. These preprocess the haystack to create skip table to advance
the pointer to next possible point.

KMP has time complxity of O(n) given preprocessing time of O(m);

Boyer-Mooer has time complexity of O(m/n) in best case; O(m * n) in worst.

Here, a simple search algorithm that can achieve O(n + m) average time
complexity is using Rabin-Karp or hash method. Naive computation of hashing
each substring of length of needle will take O(m) time, but by using rolling
hash and use the previous hash value, we can reduce it to constant. In short,

```
    hash(s[i:m]) = hash(s[i+1:m+1]) - hash(s[i]) + hash(s[i+m])
```

---

```python

class Solution28:

    def strStr(self, haystack: str, needle: str) -> int:
        
        if not haystack and not needle or haystack and not needle:
            return 0
        elif not haystack and needle:
            return -1
        
        m, n = len(haystack), len(needle)
        
        for i in range(0, m-n+1):
            if hash(haystack[i:i+n]) == hash(needle):
                return i
            
        return -1

```
