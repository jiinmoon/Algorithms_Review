# 767. Minimum Window Subsequence

Given strings S and T, find the minimum (contiguous) substring W of S, so that
T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the
empty string "". If there are multiple such minimum-length windows, return the
one with the left-most starting index.

---

We maintain the list of our windows (start, end) by first creating a mapping
where we can find the position of the next character from any given index.

---

Python:

```python

class Solution:
    def minWindowSubsequence(self, S, T):
        nextInS = [[-1] * 26] * (len(S))
        for i in range(len(S)-1, -1, -1):
            nextInS[i][ord(S[i]) - ord('a')] = i

        windows = [[i,i] for i, c in enumerate(S) if c == T[0]]

        if not windows:
            return ""

        for char in T[1:]:
            temp = list()
            for srt, end in windows:
                newEnd = nextInS[end][ord(char) - ord('a')]
                if newEnd >= 0:
                    temp.append([srt,newEnd])
            if not temp:
                return ""
            windows = temp

        srt, end = min(windows, key=lambda win: win[1] - win[0])
        return S[srt:end+1]
```
