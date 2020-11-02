# 126 Word Ladder II

Same approach - using BFS to find the shortest route between start position to
the goal. Here, use bi-directional BFS to avoid worst case.

---

Python:

```python

from collections import defaultdict

class Solution:
    def wordLadder(self, begin, end, words):
        words = set(words)
        if end not in words:
            return []

        f, b = {begin}, {end}
        fp, bp = defaultdict(set), defaultdict(set)
        swapped = False

        while f and b and not (f & b):
            if len(f) > len(b):
                f, b = b, f
                fp, bp = bp, fp
                swapped = not swapped

            newf = defaultdict(set)
            for word in f:
                for char in string.ascii_lowercase:
                    for i in range(len(word)):
                        wild = word[:i] + char + word[i+1:]
                        if wild in words and wild not in fp:
                            newf[wild].add(word)

            fp.update(newf)
            f = newf.values()

        if swapped:
            f, b = b, f
            fp, bp = bp, fp

        res = [[r] for r in f & b]
        while res and res[0][0] != begin:
            res = [[p] + r for r in res for p in fp[res[0]]]
        while res and res[0][-1] != end:
            res = [r + [p] for r in res for p in bp[res[-1]]]

        return res
```
