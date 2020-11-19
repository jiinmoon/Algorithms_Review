# 299. Bulls and Cows

You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is.
When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct
position.
The number of "cows", which are digits in the guess that are in your secret
number but are located in the wrong position. Specifically, the non-bull digits
in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint
for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is
the number of cows. Note that both secret and guess may contain duplicate
digits.

---

Counting the bulls is a simple process of counting the number of characters
that match up between guess and secret.

Counting the cows however is more involved; we first need to count each of the
characters that we seen from secret and guess. Then, for each character that we
have seen from our guess, we should check against the character map of secret.
Here, we need to take care that where characters are mapped - there may be
duplicate characters present. So, the number of cows for certain character
which is a character that is present in both but at different place should be
as much as minimum of the character count of guess and secret.

The process should complete in O(m + n).

---

Python:

```python

from collections import Counter

class Solution:
    def getHint(self, secret, guess):
        bulls = 0
        secretCount, guessCount = defaultdict(int), defaultdict(int)
        for c1, c2 in zip(secret, guess):
            if c1 == c2:
                bulls += 1
                continue
            secretCount[c1] += 1
            guessCount[c2] += 1
        
        cows = sum(min(secretCount[char], count) for char, count in guessCount.items())

        return "{}A{}B".format(bulls, cows)
```

