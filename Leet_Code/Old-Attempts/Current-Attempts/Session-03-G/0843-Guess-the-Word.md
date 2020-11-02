# 843 Guess the Word

Since we receive information about the number of positions that our guess is
corret, we find the next best candidate by word with maximum number of
positions that are same as the previous.

---

Python:

```python

class Solution:
    def guessWord(self, master, words):
        def overlapCount(w1, w2):
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        def bestGuess():
            charCounter = [defaultdict(int) for _ in range(6)]
            for word in words:
                for i, c in enumerate(word):
                    charCounter[i][c] += 1
            return max(words, key = lambda w: sum(charCounter[i][c] for i, c in enumerate(w)))

        for _ in range(10):
            curr = bestGuess()
            res = master.guess(curr)
            if res == 6:
                return
            words = [w for w in words if overlapCount(w, curr) == res]
```
