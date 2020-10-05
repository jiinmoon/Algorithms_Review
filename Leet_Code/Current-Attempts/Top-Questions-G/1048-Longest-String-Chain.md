# 1048 Longest String Chain

Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one
letter anywhere in word1 to make it equal to word2.  For example, "abc" is
a predecessor of "abac".

A word chain is a sequence of words [word\_1, word\_2, ..., word\_k] with k >= 1,
where word\_1 is a predecessor of word\_2, word\_2 is a predecessor of word\_3, and
so on.

Return the longest possible length of a word chain with words chosen from the
given list of words.

---

We create a hashmap of counting of every subword that we build as we iterate on
the words in the order of shortest to longest word. Then, we can check whether
current word's subword count to update the current to build them up.

---

Python:

```python

from collections import defaultdict

class Solution:
    def longestStrChain(self, words):
        counter = defaultdict(int)
        longest = 0

        for word in sorted(words, key=len):
            for i in range(len(word)):
                subword = word[:i] + word[i+1:]
                count = 1 + counter[subword]
                counter[word] = max(counter[word], count)
                longest = max(longest, counter[word])
        return longest
```
