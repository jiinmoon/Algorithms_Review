126 Word Letter II
==================

Given two words (beginWord and endWord), and a dictionary's word list, find all
shortest transformation sequence(s) from beginWord to endWord, such that:

- Only one letter can be changed at a time.
- Each transformed word must exist in the word list. 
- Note that beginWord is not a transformed word.

Note:

- Return an empty list if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume beginWord and endWord are non-empty and are not the same.

---

We can view this problem as a graph problem where each node is word and edge is
formed between nodes if their char differ at one place. Thus, we can perform
path finding algorithms to find the route to the start to goal if exists.

In this case, we will use bidirectional BFS which will take O(b^(d/2)) time
complexity where b is the branching factor, and d for depth.

---

Python:

Bidirectional BFS approach.

```python
from collections import defaultdict
import string

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return []
        front, back = {beginWord}, {endWord}
        # tracks words to its parents.
        # i.e. { "hot" : "hit", "cog", "dog" }
        frontParents, backParents = defaultdict(set), defaultdict(set)
        swapped = False
        
        # traverse until we have overlap or we do not have ladder.
        while front and back and not (front & back):
            # work with smaller frontier - consider branching factors.
            if len(back) < len(front):
                front, back = back, front
                frontParents, backParents = backParents, frontParents
                swapped = not swapped
            
            nextFront = defaultdict(set)
            for word in front:
                for c in string.ascii_lowercase:
                    for i in range(len(word)):
                        # find all words where differs at most on char
                        nextWord = word[:i] + c word[i+1]
                        # is word valid?
                        if nextWord in wordList and nextWord not in frontParents:
                            nextFront[nextWord] = word
            
            # update parent record and advance front
            frontParents.update(nextFront)
            front = set(nextFront.keys())

        # swap it back; it will mess up the where we begin and end.
        if swapped:
            front, back = back, front
            frontParents, backParents = backParents, frontParents

        # build result lists from centre.
        res = [[word] for word in front & back]
        while res and res[0][0] is not beginWord:
            res = [[p] + r for r in res for p in frontParents[r[0]]]
        while res and res[0][-1] is not endWord:
            res = [r + [p] for r in res for p in backParents[r[-1]]]
        return res
```
