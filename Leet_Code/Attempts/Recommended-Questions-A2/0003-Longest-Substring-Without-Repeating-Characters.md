# 3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating
characters.

---

Here, we use hashmap to maintain the previously seen characters and their
indicies. Each character is considered as an new character that we are
building; if it is a repeat, we increment our starting position of the
substring as the previously seen index of the repeat character.

---

Python:

```pyton

class Solution3:

    def longestSubstrWithoutRepeats(self, s):
        
        d = dict()
        start, result = 0, 0
        for end, char in enumerate(s):
            if char in d:
                start = max(start, d[char] + 1)
            d[char] = end
            result = max(result, end - start + 1)

        return result
```
