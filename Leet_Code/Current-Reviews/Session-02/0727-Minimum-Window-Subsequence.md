727 Minimum Window Subsequence
==============================

Given strings S and T, find the minimum (contiguous) substring W of S, so that
T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the
empty string "". If there are multiple such minimum-length windows, return the
one with the left-most starting index.

---

We first gather all the "window" which consists of index i, and j in the
S where i is the first matching occurrence of T[0], and j will expand as far as
it matches the character in T.

To enable this, we need to prepare a extra record where we will store the next
occurrence of letters in the S such that we do not have to iterate continously
to find the index of its occurrence. We can use 2D array - array[i][j] will use
to find the next occurrence of letter j in S[i+1:].

Then, we iterate on the T char by char. And for each char, we iterate on every
window to check whether we can expand the window by checking the character in
the 2D array we have built - array[endIndex][charInT] will denote the new end
index for our current window (startIndex, endIndex) - and only when the new end
index is valid (greater than 0) we can update it and add back to the list.

There may be multiple windows found in the end - among these we pick the
minimum.

Time complexity should be O(m * n) since for every char in T we exaimne the
chars in S in worst case (where all chars are equal to each other).

---

Python:

```python
class Solution:
    def minWindow(self, S, T):
        N = len(S)
        # A[i][j] maps indicies of last letter j in S[i+1:]
        lastCharIndexInS = [ None for _ in range(N) ]
        # 26 characters and its value is the last index in S
        nextCharIndex = [ -1 for _ in range(26) ]
        # iterate from behind to record the last indicies of each char in S
        for i in range(N-1, -1, -1):
            lastCharIndexInS{i] = nextCharIndex.copy()
            nextCharIndex[ord(S[i]) - ord('a')] = i
        
        # list of windows (srt, end) where
        # S[srt] matches the first char in T
        # S[end] matches the current char in T to be expanded
        windows = [ [i,i] for i, c in enumerate(S) if c == T[0] ]

        if not windows: return ""

        for c in T[1:]:
            nextWindows = list()

            for srt, end in windows:
                # find last occurrence of char in T, "c" in S
                # starting from S[end+1:]
                newEnd = lastCharIndexInS[end][ord(c) - ord('a')]
                if newEnd >= 0:
                    newWindows.append( (srt, newEnd) )

            if not newWindows: return ""
            windows = newWindows

        minSrt, minEnd = min(windows, key = lambda w : w[1]-w[0])
        return S[minSrt:minEnd+1)
```

