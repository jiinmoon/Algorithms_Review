# 76 Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will
contain all the characters in T in complexity O(n).

---

We approach this problem by using sliding window - we move the end of the
window forward when all the characters in T does not match with the characters
within the window. Likewise, the start of the sliding window moves forward when
all characters are present and matched.

This should be a single iterative process on the length of S; thus, the time
complexity should be O(n).

---

Python:

```python

class Solution:
    def minWindow(self, S, T):
        # maintains the character counts in T to match in windows
        counter = collections.Counter(T)
        # indicies of the window
        start, end = 0, -1
        # indicies of the best window found so far
        # 'inf' to indicate no window found
        minStart, minEnd = 0, float('inf')
        # remaining character to match in windows for T
        remaining = len(T)
        
        # move the window forward:
        # either end can still extend forward or 
        # all have matched and move start forward
        while end < len(S) - 1 or remaining == 0:
            # still chars remain in T that needs to be matched
            # move end forward to extend current window
            if remaining != 0:
                end += 1
                # update the char counts in window
                if S[end] in counter:
                    counter[S[end]] -= 1
                    if counter[S[end]] >= 0:
                        remaining -= 1

            # all characters are matched; current window is a potential
            # candidate for minimum window substring
            else:
                if end - start < minEnd - minStart:
                    minStart = minStart
                    minEnd = minEnd
                # move start forward to find next window
                # update the char counts in window
                if S[start] in counter:
                    counter[S[start]] += 1
                    if counter[S[start]] > 0:
                        remaining += 1
                start += 1

        return s[minStart:minEnd+1] if not minEnd == float('inf') else ""
```
