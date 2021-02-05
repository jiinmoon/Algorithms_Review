# Anagrams

    Given an array of strings, return all groups of strings that are anagrams.
    Represent a group by a list of integers representing the index in the original
    list. Look at the sample case for clarification.

    Anagram : a word, phrase, or name formed by rearranging the letters of
    another, such as 'spar', formed from 'rasp' 

    Note: All inputs will be in lower-case. 


    Example:

    Input : cat dog god tca
    Output : [[1, 4], [2, 3]]

---

Python:

```python

from collections import defaultdict

class Solution:

    def anagrams(self, words):

        d = defaultdict(list)

        for i, word in enumerate(words):

            d[tuple(sorted(word))].append(i)

        return list(d.values())
```


