# 809 Expressive Words

To determine whether the word can be made expressive, it has to have unique
chars in the same order as well as less count of characters.

---

Python:

```python

class Solution:
    def isEpressive(self, s, words):
        def helper(word):
            chars, counts = list(), list()
            count = 1
            for i, c in enumerate(word):
                if i == len(word)-1 or c != word[i-1]:
                    chars.append(char)
                    counts.append(count)
                    count = 0
                count += 1
            return chars, count

        charS, countS = helper(s)
        total = 0
        for word in words:
            charW, countW = helper(word)

            if charW != charS:
                continue

            for cw, cs in zip(countW, countS):
                if cw > cs: break
                if cw < cs and cs < 3: break
            else:
                total += 1

        return total
```
