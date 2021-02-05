1048 Longest String Chain
=========================

Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one
letter anywhere in word1 to make it equal to word2.  For example, "abc" is
a predecessor of "abac".

A word chain is a sequence of words `[word_1, word_2, ..., word_k]` with k >= 1,
where `word_1` is a predecessor of `word_2`, `word_2` is a predecessor of
`word_3`, and so on.

Return the longest possisble length of a word chain with words chosen from the
given list of `words`.

---

The approach is as follows:

We first sort the given list of words by their lengths. Then, we examine each
of the word and decontruct it to smaller word with a character removed at every
location. We record the occurrence of each of these smaller word into the
hashmap and compute the max length we have seen thus far.

Hence, at every word, we look up this record for whether the previous smaller
word has been in there - and how many times that it has occurred from various
words that came before this word.

The time complexity of this algorithm would be O(n * k^2): for each word, we
have to break it down to every possible way (k^2 possible smaller words exist).

---

Python:

```python
from collections import defaultdict

class Solution:
    def longestStrChain(self, words):
        if not words:
            return 0

        prevSubwordCount = defaultdict(int)
        longestThusFar = 0
        for w in sorted(words, key=len):
            for i in range(len(w)):
                subword = w[:i] + w[i+1:]
                # count current as well
                count = prevSubwordCount[subword] + 1
                # record the count
                prevSubwordCount[word] = max(prevSubwordCount[word], count)
                # maintain longest we have seen so far
                longestThusFar = max(longestThusFar, prevSubwordCount[word])

        return longestThusFar
```



