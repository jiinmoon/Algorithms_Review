# 76. Minimum Window Substring

Given two strings s and t, return the minimum window in s which will contain
all the characters in t. If there is no such window in s that covers all
characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be
only one unique minimum window in s.

---

To find the minimum window substring where it contains all characters from the
another, we try to maintain the window start and end points - and update the
minimum start end end points that has been found thus far. Since the order does
not matter, we simply create a hashmap counter of all characters in the t, and
update it as we iterate forward on the given string s. This algorithm should be
of O(n) in time complexity.

---

```python

class Solution:
    def minimumWindowSubstring(self, s, t):
        counter = collections.Counter(t)
        start, end = 0, -1
        minStart, minEnd = 0, float('-inf')
        matching = len(t)

        while end < len(s) - 1 or matching == 0:
            # more characters to find in s
            if matching:
                # add new character in the end
                # update the counter
                end += 1
                if s[end] in counter:
                    counter[s[end]] -= 1
                    if counter[s[end]] >= 0:
                        matching -= 1
            # all characters are found in s
            else:
                # update the min window size thus far
                if end - start < minEnd - minStart:
                    minStart = start
                    minEnd = end
                # remove start the update the counter
                # (return start char back to the pool)
                if s[start] in counter:
                    counter[s[start]] += 1
                    if counter[s[start]] > 0:
                        matching += 1
                start += 1

        return s[minStart:minEnd+1] if minEnd != float('-inf') else ""
```
