# 127 Word Ladder

We can use BFS to find the shortest route.

---

Python:

```python

class Solution:
    def wordLadder(self, begin, end, words):
        words = set(words)
        if end not in words:
            return -1

        length = 1
        f, b = {begin}, {end}
        visited = set()

        g = collections.defaultdict(set)
        for word in words:
            for i in range(len(word)):
                wild = word[:i] + "." + word[i+1:]
                g[wild].append(word)

        while f and b:
            if f & b:
                return length

            newf = set()
            for word in f:
                visited.add(word)
                for i in range(len(word)):
                    wild = word[:i] + "." + word[i+1:]
                    nextWords = g[wild]
                    nextWords -= visited
                    newf |= nextWords

            f = newf
            length += 1

            if len(f) > len(b):
                f, b = b, f

        return -1
```
