# 727 Minimum Window Subsequence

Given strings S and T, find the minimum (contiguous) substring W of S, so that
T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the
empty string "". If there are multiple such minimum-length windows, return the
one with the left-most starting index.

---

We maintain a list of windows that will grow at the end, for each starting
positions that we can exaimne so long as the beginning character matches that
another. To enable this, we create a hashmap that records the indicies of each
of the characters appearing the in string.

---

Python:

```python

class Solution:
    def minWindows(self, S, T):
        nextInS = [[-1 for _ in range(26)] for _ in range(len(S))]
        for i in range(len(S)-1, -1, -1):
            nextInS[i][ord(S[i])-ord('a')] = i

        windows = [(i,i) for i, c in enumerate(S) if c == T[0]]
        if not windows:
            return ""

        for char in T[1:]:
            temp = list()
            for start, end in windows:
                newEnd = nextInS[end][ord(char)-ord('a')]
                if newEnd >= 0:
                    temp.append( (start,newEnd) )

            if not temp:
                return ""

            windows = temp

        start, end = min(windows, key=lambda w : w[1] - w[0])
        return S[start:end+1]
```
