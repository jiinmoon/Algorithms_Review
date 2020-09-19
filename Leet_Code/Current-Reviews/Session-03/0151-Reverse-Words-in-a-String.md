151 Reverse Words in a String
=============================

Given an input string, reverse the string word by word.

---

This is a rather trivial question if we are using the right langauge or know
the right string library. If these are unaviliable, other option is to simply
traverse the string char by char - building a word so long as what we are
seeing is an alphabet. Once we have all the words identified, we can reverse
the entire container and then concatenate the words.

---

Python:

```python
class Solution:
    def reverseWords(self, s):
        return " ".join(s.strip().split()[::-1])
```
