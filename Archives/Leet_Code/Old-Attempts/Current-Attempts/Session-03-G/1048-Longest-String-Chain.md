# 1048 Longest String Chain

Starting from the smallest word, we build up the counter for each of the
subword that can be formed from the word.

---

Python:

```python

class Solution:
    def longestStringChain(self, words):
        counter = collections.defaultdict(int)
        longest = 0

        for word in sorted(words, key=len):
            subword = word[:i] + word[i+1:]
            count = 1 + counter[subword]
            counter[word] = max(counter[word], count)
            longest = max(longest, counter[word])

        return longest
```
