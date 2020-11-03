# 819. Most Common Word

Given a paragraph and a list of banned words, return the most frequent word
that is not in the list of banned words.  It is guaranteed there is at least
one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of
punctuation.  Words in the paragraph are not case sensitive.  The answer is in
lowercase.

---

The first problem that we encounter here would be to sanitizing the
non-character values to split the given paragraph into list of words. This can
be done with the regex substitution of replacing any non-character(not
A-Za-z0-0) with a whitespace. And then spliting the clean string by the
whitespace characters. Once we have the list of words, we can create the
counter mapping of word to count while checking that each word is not in the
list of banned words.

---

Python:

```python

import re

class Solution:
    def mostCommonWords(self, paragraph, banned):
        banned = set(banned)
        banned.add("")
        words = re.sub("[^A-Za-z0-9]", " ", paragraph).lower().split(" ")
        counter = collections.Counter([word for word in words if word not in banned])
        return max(counter.items(), key=x : x[1])[0] 
```
