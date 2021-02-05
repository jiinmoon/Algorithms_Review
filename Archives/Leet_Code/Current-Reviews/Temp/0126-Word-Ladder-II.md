# 126. Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all
shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not
a transformed word.


Note:

Return an empty list if there is no such transformation sequence.

All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

---

We can find the shortest path or transformation sequence between nodes or words
via using BFS algorithm - namely, we can use a bidirectional BFS. Starting from
beginWord and endWord, we try to expand out to next nodes until they meet. To
build the path, we maintain hashmap of parents where each node's parent will be
recorded.

Time complexity would be typical of bidirectional BFS which is O(b ^ (d / 2))
where b is the branching factor and d is the distance of the path between two
nodes. Space complexity would be O(d) where d is the length of the path
explored.

---

Python:

```python

from collections import defaultdict

class Solution126:

    def findLadders(self, beginWord, endWord, wordList):

        wordList = set(wordList)

        if endWord not in wordList:
            return []

        front, back = {beginWord}, {endWord}
        # stores set of parents for a word
        frontParents, backParents = defaultdict(set), defaultdict(set)
        # requires to swap back to identify front from back
        isSwapped = False

        while front and back and not (front & back):

            newFront = defaultdict(set)

            for word in front:
                for i in range(len(word)):
                    for c in string.asci_lowercase:
                        wild = word[:i] + c + word[i+1:]
                        if wild in wordList and wild not in frontParents:
                            newFront[wild].add(word)

            frontParents.update(newFront)
            front = set(newFront.keys())

            if len(front) > len(back):
                front, back = back, front
                frontParents, backParents = backParents, frontParents
                isSwapped = not isSwapped

        if isSwapped:
            front, back = back, front
            frontParents, backParents = backparents, frontParents
        
        # start gathering from overlapping nodes
        result = [[r] for r in (front & back)]

        # build to front parent until beginWord
        while result and result[0][0] != beginWord:
            result = [[p] + r for r in result for p in frontParents[r[0]]]

        # build to back parent until endWord
        while result and result[0][-1] != endWord:
            result = [r + [p] for r in result for p in backParents[r[-1]]]

        return result
```
