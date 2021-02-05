# 727 Minimum Window Subsequence

We maintain the sliding windows; for every char, we extend out so long as we
can find the char in next. To do so, we first create the list of indicies for
each char that comes after words. So, when we examine the sliding window, we
can easily look up where the char may appear after the end of the sliding
window to compute new end window.

---

Python:

```python

class Solution:
    def minWindowSubsequence(self, S, T):
        nextInS = [[-1 for _ in range(26)] for _ in range(len(S))]
        for i in range(len(S)-1, -1, -1):
            nextInS[i][ord(S[i])] = i

        windows = [(i,i) for i, c in enumerate(S) if c == T[0]]
        if not windows:
            return ""

        for char in T[1:]:
            temp = list()
            for srt, end in windows:
                newEnd = nextInS[end][ord(char) - ord('a')]
                if newEnd >= 0:
                    temp.append((srt,newEnd))
            if not temp:
                return ""

        srt, end = min(windows, key=lambda w: w[1] - w[0])
        return S[srt:end+1]
```
