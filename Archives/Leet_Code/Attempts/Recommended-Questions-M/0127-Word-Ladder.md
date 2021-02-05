# 127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the
length of shortest transformation sequence from beginWord to endWord, such
that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

---

This problem is best visualized as a graph problem where each node is the word
and the edges form between the words iff it can transform into one another.
Then, finding the shortest path from start node to the end node is done with
the BFS algorithm. In particular, we can use a bidirectional BFS to avoid the
worst case scenario of exploring only from the path where the branching factor
is skwed. Hence, the time complexity can be reduced to O(b ^ (d/2)) where b is
the branching factor (average num of edges to explore) and d is the depth of
the path taken.

---

Python:

```python

class Solution:
    def wordLadder(self, begin, end, words):
        words = set(words)
        if end not in words:
            return 0

        f, b, visited = {begin}, {end}, {}
        length = 1

        g = collections.defaultdict(set)
        for word in words:
            for i in range(len(word)):
                wild = word[:i] + "." + word[i+1:]
                g[wild].add(word)

        while f:
            if f & b:
                return length

            if len(f) > len(b):
                f, b = b, f

            newf = set()
            for word in f:
                visited.add(word)
                for i in range(len(word)):
                    wild = word[:i] + "." + word[i+1:]
                    neighbours = g[wild]
                    neighbours -= visited
                    newf |= neighbours

            f = neighbours
            length += 1

        return 0
```
