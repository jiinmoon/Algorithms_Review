# 843 Guess the Word

from collections import defaultdict

class Solution:
    def guessWord(self, master, words):
        def overlapCount(w1, w2):
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        def bestGuess():
            charCount = [defaultdict(int) for _ in range(6)]
            for word in words:
                for i, c in enumerate(words):
                    charCount[i][c] += 1

            return max(words, key=lambda w : sum(charCounter[i][c] for i, c in enumerate(w)))

        for _ in range(10):
            curr = bestGuess()
            res = master.guess(curr)
            if res == 6:
                return
            words = [w for w in words if overlapCount(w, curr) == res]
