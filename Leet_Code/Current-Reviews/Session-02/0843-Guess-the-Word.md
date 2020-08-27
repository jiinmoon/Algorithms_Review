843 Guess the Word
==================

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

The problem at first glance appears to be completely random - but fact that
each wrong guess returns the current matching number of characters allows us to
eliminate the words more rapidly to pick a better candidate in next try.

At each occasion, we try to take our best guess. Among the candidates, we pick
the candidate word that has the most number of overlapping characters with
others. This is determined by maintaining how often a char at index i appears
amongst all the words (array of hashmap<char, int>).

When we fail our guess, we receive a number of matching characters from our
guess to the secret word. This allows us to screen out the candidates by
choosing only the candidate with same number of overlapping characters.

---

```python
# class Master:
#   def guess(self, word: str) -> int:

from collections import defaultdict

class Solution:
    def findSecretWord(self, wordlist, master):
        candidates = wordlist
        count = 10
        
        # sum of overlapping characters between two words
        def overlapCount(word1, word2):
            return sum(c1 == c2 for c1, c2 in zip(word1, word2))

        # best candidate is the one with "overall" highest overlap counts
        def bestGuess():
            charCounter = [ defaultdict(int) for _ in range (6) ]
            for candidate in candidates:
                for i, char in enumerate(candidate):
                    charCounter[i][char] += 1

            return max(
                    candidates,
                    key = lambda candidate :
                                sum(charCounter[i][c] for i, c in enumerate(candidate))

        # begin guessing
        while candidates or count != 0:
            currGuess = bestGuess()
            result = master.guess(currGuess)
            if result == 6:
                return # happy happy
            # update candidates with those that have same "overall" number of overlapping characters
            candidates = [ candidate for candidate in candiates if
                                overlapCount(candidates, currGuess) == result]
```

