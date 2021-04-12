# 127. Word Ladder

A transformation sequence from word beginWord to word endWord using
a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk
such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to
be in wordList.
sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the
number of words in the shortest transformation sequence from beginWord to
endWord, or 0 if no such sequence exists.

---

Same problem as 126, but we can simplify bits of our algorithm where we
maintain the connections to the parent nodes as we no longer have to return the
entire list of words in the path - but only have to maintain the length of the
path that we have taken to reach the goal. 

---

Python:

```python

class Solution127:

    def wordLadder(self, words, start, end):

        words = set(words)

        if not (words and end in words):
            return 0

        front, back = {}, {}
        length = 1

        while front:
            
            tempQueue = set()

            for word in front:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        nextWord = word[:i] + c + word[i+1:]
                        # goal reached
                        if nextWord in back:
                            return length + 1
                        if nextWord in words:
                            words.remove(nextWord)
                            tempQueue.add(nextWord)
            
            if len(front) > len(back):
                front, back = back, tempQueue
            else:
                front = tempQueue

            length += 1

        return 0
```

