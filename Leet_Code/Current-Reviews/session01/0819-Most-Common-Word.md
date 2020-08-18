819 Most Common Word
====================

Given a paragraph and a list of banned words, return the most frequent word
that is not in the list of banned words. It is guranteed there is at least one
word that isn't banned and that the answer is unique.

---

Create a set of words from the given paragraph. Then, remove the set of banned
words and count the frequency of the words. It may seem easy but cleaning the
given string is more troublesome than one might expect (i.e. think of cases
such as "a, a, a, b,b,b,b,c, a, c"). For this, we will use regular expression
instead.

---

Python:

```python
from collecitons import defaultdict
import re

class Solution:
    def mostCommonWord(self, paragragh, banned):
        counter = defaultdict(int)
        banned = set(banned)
        # to later detect split on whitespace
        banned.add('')
        # substitute non-alnum with whitespaces
        paragraph = re.Sub('[A-Za-z0-9]}', ' ', paragraph)
        for word in paragraph.lower().split(' '):
            if word not in banned:
                counter[word] += 1
        return max(counter.items(), key=lambda x: x[1])[0]
```
