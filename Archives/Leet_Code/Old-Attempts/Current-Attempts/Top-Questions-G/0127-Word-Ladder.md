# 127 Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the
length of shortest transformation sequence from beginWord to endWord, such
that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.

---

We can view this problem as a graph problem where each node is word and edges
represent a relationship where two words differ at a single character. Thus,
from start to goal, we perform BFS to find the shortest path. Here, we use
bidirectional bfs to avoid the worst case as well as improve the time
complexity by half of the branching factor.

---

Python:

```python

from collections import defaultdict

class Solution:
    def wordLadder(self, begin, end, words):
        words = set(words)
        if end not in words:
            return 0

        f, b, visited = {begin}, {end}, {}
        g = defaultdict(set)
        for word in words:
            for i in range(len(word)):
                wild = word[:i] + "." + word[i+1:]
                g[wild].add(word)
        
        length = 1
        while f and b:
            if f & b:
                return length

            newf = set()
            for word in f:
                visited.add(word)
                for i in range(len(word)):
                    wild = word[:i] + "." + word[i+1:]
                    nextWords = g[wild]
                    newf |= nextWords - visited
            f = newf
            length += 1

            if len(f) > len(b):
                f, b = b, f

        return 0
```
