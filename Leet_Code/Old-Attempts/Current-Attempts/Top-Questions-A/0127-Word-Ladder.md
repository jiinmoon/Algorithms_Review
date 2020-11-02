# 127 Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the
length of shortest transformation sequence from beginWord to endWord, such
that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.

---

Finding the shortest path from start to goal can be done via BFS algorithm - we
treat this as a graph problem where each word is the node and edges are formed
when only one letter can be changed to become another word. Here, we use
a improved version of the BFS that is bidirectional - starting from both end of
the start and goal to see whether the there exists a path.

The time complexity of the bidirectional BFS can be drastically reduced from
that of normal BFS since it can avoid taking the route of dense branches.
Suppose that the distance from start to goal is "d" and branching factor is
"b", then regular BFS will cost O(b^d). But, with bidirecitonal BFS, we reduce
the distance by half - which is O(b^d/2 + b^d/2).

---

Python:

```python

class Solution:
    def wordLadder(self, beginWord, endWord, words):
        words = set(words)
        if endWord not in words:
            return 0

        steps = 1
        f, b, visited = {beginWord}, {endWord}, {}
        g = collections.defaultdict(set)
        for word in words:
            for i in range(len(word)):
                g[word[:i] + "." + word[i+1:]].add(word)

        while f:
            if f & b:
                return steps

            newf = set()
            for word in f:
                visited.add(word)
                for i in range(len(word)):
                    nextWords = g[word[:i] + "." + word[i+1:]]
                    nextWords -= visited
                    newf |= nextWords

            f = nextWords
            steps += 1

            if len(f) > len(b):
                f, b = b, f

        return 0
```
