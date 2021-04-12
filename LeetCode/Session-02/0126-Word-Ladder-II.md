# 126. Word Ladder II

A transformation sequence from word beginWord to word endWord using
a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk
such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to
be in wordList.
sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return all
the shortest transformation sequences from beginWord to endWord, or an empty
list if no such sequence exists. Each sequence should be returned as a list of
the words [beginWord, s1, s2, ..., sk].

---

This problem can be visualized as a graph problem where we are trying to find
the shortest path between two nodes - where each vertices represent a word and
an edge is formed between verticies iff there exists a connection (differ by at
most one character).

There are several algorithms to find the shortest path in graph but popular
ones are A* star which uses heuristic to determine how close that we are
approaching the goal and BFS.

Here, we will use bidirectional BFS as it can avoid worst case scenario of
selecting the path where branching factor is too severe to explore.

---

Python:

```python

from collections import defaultdict

class Solution126:

    def wordLadder(self, words, begin, end):

        words = set(words)

        if end not in words:
            return []

        # two queues for "bi"-direction BFS
        front, back = { front }, { end }
        # hashmap to track parent nodes to collect in the end
        frontParent, backParent = defaultdict(set), defaultdict(set)
        # we are to swap back and forth between front and back
        # need an indicator to properly set front from back in the end
        isSwapped = False
        
        # until we have no overlap
        while front and back and not (front & back):
            
            tempQueue = defaultdict(set)

            for word in front:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        nextWord = word[:i] + c + word[i+1:]
                        if nextWord in words and nextWord not in frontParent:
                            tempQueue[nextWord].add(word)

            frontParent.update(tempQueue)
            front = set(tempQueue.keys())

            if len(front) > len(back):
                isSwapped = not isSwapped
                front, back = back, front
                frontParent, backParent = backParent, frontParent

        if isSwapped:
            front, back = back, front
            frontParent, backParent = backParent, frontParent
        
        # start from the middle of path (overlap of two queues)
        result = [ [node] for node in front & back ]
        # expand to begin word
        while result and result[0][0] != begin:
            result = [ [p] + node for node in result for p in frontParent[node[0]] ]
        # expand to end word
        while result and result[0][-1] != end:
            result = [ node + [p] for node in result for p in backParent[node[-1]] ]

        return result
```

