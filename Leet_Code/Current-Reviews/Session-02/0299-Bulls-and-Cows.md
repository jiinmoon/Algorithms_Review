299 Bulls and Cows
==================

You are playing the following Bulls and Cows game with your friend: You write
down a number and ask your friend to guess what the number is. Each time your
friend makes a guess, you provide a hint that indicates how many digits in said
guess match your secret number exactly in both digit and position (called
"bulls") and how many digits match the secret number but locate in the wrong
position (called "cows"). Your friend will use successive guesses and hints to
eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's
guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate
digits.

---

The bulls can be easily found by iterating on both characters in secret and
guess - and count the matching characters.

As for the cows, we need a way to check whether the char in guess occurs in
secret - and we need a way to maintain a record where we record only the
characters that have not matched (which is used up when counting the bulls).
Hence, we use hashmap to record each of the unmatched characters in secret and
guess. The cows will then be the minimum occurrence of the unmatched characters
in record of guess and record of secret.

The time complexity should be linear.

---

Python:

```python
from collections import defaultdict

class Solution:
    def getHint(self, secret, guess):
        sCount, gCount = defaultdict(), defaultdict()
        bulls, cows = 0, 0

        for cs, cg in zip(secret, guess):
            if cs == cg:
                bulls += 1
                continue
            sCount[cs] += 1
            gCount[cg] += 1

        cows = sum(min(sCount[g], count) for g, count in gCount.items())

        return "{}A{}B".format(bulls, cows)
```

