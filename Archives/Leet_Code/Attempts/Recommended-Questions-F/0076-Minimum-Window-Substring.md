# 76. Minimum Window Substring

Given two strings s and t, return the minimum window in s which will contain
all the characters in t. If there is no such window in s that covers all
characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be
only one unique minimum window in s.

---

Since the important point here is that order of the characters in t does not
matter, we use a hashmap to count the individual characters that we are
examining thus far. As we iterate forward, we update our counter to see that it
is balanced - if so, then we record the current matching substring and find the
minimum amongst them.

Time complexity is O(n) and it is same for space complexity.

---

Java:

```java




``` 


Python:

```python

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = collections.Counter(t)
        start, end = 0, -1
        minStart, minEnd = 0, float('inf')
        match = len(t)
        
        while end < len(s)-1 or match == 0:
            if match:
                end += 1
                if s[end] in counter:
                    counter[s[end]] -= 1
                    if counter[s[end]] >= 0:
                        match -= 1
            else:
                if end - start < minEnd - minStart:
                    minStart = start
                    minEnd = end
                if s[start] in counter:
                    counter[s[start]] += 1
                    if counter[s[start]] > 0:
                        match += 1
                start += 1
        
        if minEnd == float('inf'):
            return ""
        return s[minStart:minEnd+1]

```
