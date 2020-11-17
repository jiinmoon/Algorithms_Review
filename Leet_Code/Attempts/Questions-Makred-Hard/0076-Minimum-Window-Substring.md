# 76. Minimum Window Substring

Given two strings s and t, return the minimum window in s which will contain
all the characters in t. If there is no such window in s that covers all
characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be
only one unique minimum window in s.

---

Here, we are trying to find the minimum sized window (substring) that contains
all characters from one to another. Then, we can approach this problem as
a sliding window problem. At each iteration, we try to add our character and
remove the character from either ends to check to see whether we have our
substring matched. To easily check for the condition, we can use hashmap to
maintain our character counts.

The time complexity is O(n).

---

Python:

```
class Solution:
    def minWindowSubstring(self, s, t):
        counter = collections.Counter(t)
        # current window positions
        start, end = 0, -1
        minStart, minEnd = 0, float('inf')
        toMatch = len(t)

        while end < len(s) - 1 or not toMatch:
            # still more characters to match
            if toMatch:
                end += 1
                # remove to match s[end] to pool
                if s[end] in counter:
                    counter[s[end]] -= 1
                    if counter[s[end]] >= 0:
                        toMatch -= 1
            # all characters from t are found in substring
            # between s[start:end]
            else:
                if end - start < minEnd - minStart:
                    minStart = start
                    minEnd = end
                # return first character to the pool
                if s[start] in counter:
                    counter[s[start]] += 1
                    if counter[s[start]] > 0:
                        toMatch += 1
                start += 1

        return s[minStart:minEnd+1] if minEnd != float('inf') else ""
```
