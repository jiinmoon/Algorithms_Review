# 843 Guess the Word

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

We need to be able to pick a guess at each stage that will provide the best
chance of being the secret word. After each selection, we receive a feedback of
how many characters in the correct position. If so, then when we make next
guess, we can base it on this feedback that we should choose next words which
have the same correct position as the previous guess word.

To choose the best word, we first examine the character count at each of the
words index - since there are only 6 letters long, this is a constant
operation. Then, we can choose the word that which has the highes total count.

---

Python:

```python

from collections defaultdict

class Solution:
    def findSecretWord(self, words, master):
        def overlapCount(w1, w2):
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        def nextGuess():
            charCount = [defaultdict(int) for _ in range(6)]
            for word in words:
                for i, char in enumerate(word):
                    charCount[i][char] += 1
            return max(words, key=lambda word:
                sum(charCount[i][char] for i, char in enumerate(words)))

        for _ in range(10):
            currGuess = nextGuess()
            result = master.guess(currGuess)
            if result == 6:
                return True
            words = [word for word in words if overlapCount(word, currGuess)]
```
