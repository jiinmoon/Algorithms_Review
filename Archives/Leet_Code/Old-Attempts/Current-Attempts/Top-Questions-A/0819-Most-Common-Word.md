# 819 Most Common Word

Given a paragraph and a list of banned words, return the most frequent word
that is not in the list of banned words.  It is guaranteed there is at least
one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of
punctuation.  Words in the paragraph are not case sensitive.  The answer is in
lowercase.

---

Firstable, we sanitize the given paragraph into words - we achieve this with
a regex expression that substitues all ocurrences of non-alphanumeric
characters with a space; then we can split the given paragraph into words
at each space. Then, iterate to count each frequency to find the most commonly
occuring word that is not in the banned words.

---

Python:

```python

import re

class Solution:
    def mostCommonWord(self, banned, paragraph):
        s = re.sub('[^A-Za-z0-9]+', " ", paragraph)
        banned = set(banned)
        banned.add("")
        d = collections.defaultdict(int)
        for word in paragraph.split(" ").lower():
            if word not in banned:
                d[word] += 1
        return max(d.items(), key=lambda item: item[1])[0]
```
