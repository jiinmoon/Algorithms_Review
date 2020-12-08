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

We may use bidirectional BFS search to find the length of the shortest
transformation sequence from beginWord to endWord. Time complexity would be O(b ^ (d/2)).

---

Python:

```python

class Solution127:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList = set(wordList)
        
        if endWord not in wordList:
            return 0
        
        front, back, length = {beginWord}, {endWord}, 1
        
        while front:
            
            newFront = set()
            
            for word in front:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        wild = word[:i] + c + word[i+1:]
                        
                        if wild in back:
                            return length + 1
                        
                        if wild in wordList:
                            wordList.remove(wild)
                            newFront.add(wild)
            
            if len(front) > len(back):
                front, back = back, newFront
            else:
                front = newFront
            
            length += 1
        
        return 0
```
