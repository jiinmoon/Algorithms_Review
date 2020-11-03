# 843. Guess the Word

We are given a word list of unique words, each word is 6 letters long, and one
word in this list is chosen as secret.

You may call master.guess(word) to guess a word.  The guessed word should have
type string and must be from the original list with 6 lowercase letters.

This function returns an integer type, representing the number of exact matches
(value and position) of your guess to the secret word.  Also, if your guess is
not in the given wordlist, it will return -1 instead.

For each test case, you have 10 guesses to guess the word. At the end of any
number of calls, if you have made 10 or less calls to master.guess and at least
one of these guesses was the secret, you pass the testcase.

Besides the example test case below, there will be 5 additional test cases,
each with 100 words in the word list.  The letters of each word in those
testcases were chosen independently at random from 'a' to 'z', such that every
word in the given word lists is unique.

---

At first glance, it appears to be completely random choice as to how we can
pick the correct guess. However, the fact that we receive information about the
number of places on the guess that are correct allows us to reduce the size of
the guesses - first we pick a guess. Then, we reduce the candidates by the
words that share the same number of the correct result.

---

Python:

```python

from collections import defaultdict

class Solution:
    def findSecretWord(self, wordList, master):
        def overlapCount(w1, w2):
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        def bestGuess():
            charCount = [defaultdict(int) for _ in range(6)]
            for word in wordList:
                for i, char in enumerate(word):
                    charCount[i][char] += 1
            return max(
                wordList, 
                key = lambda word : sum(charCount[i][char] for i, char in enumerate(word)))

        for _ in range(10):
            currGuess = bestGuess()
            result = master.guess(currGuess)
            if result == 6:
                return
            wordList = [word for word in wordList if overlapCount(word, currGuess) == result]

        return
```
