# 126 Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all
shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not
a transformed word.

---

Finding the shortest path from start to goal can be approached with a BFS
traversal on the graph where each node is the word and edges form between words
iff one character can be changed to form another word. Since the goal is also
known, we may perform bidirectional bfs. And since we need actual path (list of
words), we maintain a parent hashmap where each node's parent is recorded.

---

Python:

```python

from collections import defaultdict

class Solution:
    def wordLadder(self, begin, end, words):
        words = set(words):
        if end not in words:
            return []

        f, b = {begin}, {end}
        fp, bp = defaultdict(set), defaultdict(set)
        swapped = False

        while f and b and not (f & b):
            if len(f) > len(b):
                f, b = b, f
                fp, bp = bp, fp
                swapped = True

            newf = defaultdict(set)
            for word in f:
                for c in strings.ascii_lowercase:
                    for i in range(len(word)):
                        wild = word[:i] + c + word[i+1:]
                        if wild in words and wild not in fp:
                            newf[wild].add(word)

            fp.update(newf)
            f = set(newf.keys())

        if swapped:
            f, b = b, f
            fp, bp = bp, fp

        res = [[n] for n in f & b]
        while res and res[0][0] != begin:
            res = [[p] + r for r in res for p in fp[r[0]]]
        while res and res[0][-1] != end:
            res = [r + [p] for r in res for p in bp[r[-1]]]

        return res
```
