127 Word Letter
===============

Given two words (beginWord and endWord), and a dictionary's word list, find the
length of shortest transformation sequence from beginWord to endWord, such
that:

- Only one letter can be changed at a time.
- Each transformed word must exist in the word list.

Note:

- Return 0 if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

```
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog"
-> "cog",
return its length 5.
```

Example 2:

```
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible
transformation.
```

---

We can view this problem as a graph problem where each node is word and ege is
formed between nodes if their char differ at one place. Thus, we can perform
path finding algorithms to find the route to the start to goal if exists.

In this case, we will use bidirectional BFS which will take O(b^(d/2)) time
complexity where b is the branching factor, and d for depth.

---

Python:

Bidirectional BFS approach.

```python
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        length = 1
        visited = 0
        graph = defaultdict(set)
        if endWord not in wordList:
            return 0
        for word in wordList:
            for i in range(len(word)):
                wildcard = word[:i] + '.' + word[i+1:]
                graph[wildcard].add(word)
        front, back = {beginWord}, {endWord}
        while front:
            # path found; there is a bisection.
            if front & back:
                return length
            # no path found yet; build next neighbours
            newFront = set()
            for word in front:
                visited.add(word)
                for i in range(len(word)):
                    # every word differ in 1 length
                    wildcard = word[:i] + '.' + word[i+1:]
                    neighbours = graph[wildcard]
                    # take away visited
                    neighbours -= visited
                    # add to newFront
                    newFront |= neighbours
            front = newFront
            if len(front) > len(back):
                front, back = back, front 
            length += 1
        return 0
```
