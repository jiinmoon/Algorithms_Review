# 727. Minimum Window Subsequence

Given strings S and T, find the minimum (contiguous) substring W of S, so
that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the
empty string "". If there are multiple such minimum-length windows, return the
one with the left-most starting index.

---

We think of this problem as a collection of windows that expands out from each
starting positions to cover as far out as possible. To do so, we need to create
a map characters found in s; at each index, we record next index where the
character appears againt to its right.

Then, we maintain the list of windows starting from (i, i) where i are the
indicies from s where s[i] is potential starting subsequences. Then, by looking
up on the index as we iterate on every character on T, we can find all
subsequences starting and end positions. Amongst these, we pick the minimum.

Time complexity depends upon how many windows are present but worst case all
characters can be present from S and T, hence it would be O(m * n).

---

Python:

```python

class Solution:
    def minWindow(self, s, t):
        charIndicies = [ [-1 for _ in range(26)] for _ in range(len(s)) ]
        for i in range(len(s)-1, -1, -1):
            charIndicies[i][ord(s[i]) - ord('a')] = i

        windows = [(i,i) for i, c in enumerate(s) if c == t[0]]
        if not windows:
            return ""

        for char in t[1:]:
            temp = list()

            for start, end in windows:
                nextEnd = charIndicies[end][ord(char) - ord('a')]
                if nextEnd >= 0:
                    temp.append((start, nextEnd))
                
                if not temp:
                    return ""

            windows = temp

        start, end = min(windows, key = lambda window: window[1] - window[0])
        return s[start:end+1]
```

