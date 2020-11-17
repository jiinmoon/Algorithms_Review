# 1010. Pairs of Songs With Total Durations Divisible by 60

In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds
is divisible by 60.  Formally, we want the number of indices i, j such that
i < j with (time[i] + time[j]) % 60 == 0.

---

Finding pairs of song that are divisible by 60 means that their sum should be
completely divislbe by 60 (or modulo 60 with no remainders). Hence, we can
express it as a check for `(x % 60) + (y % 60) - 60 = 0`.

So, we prepare a count map using hashmap; when we are examning each song,
compute its modulo 60 to record its count. Then, we can find whether the
counterpart that can sum to be divisble by 60 by looking up the record.

The time complexity and space complexity are O(n).

---

Python:

```python

class Solution:
    def findPairsDivisibleBy60(self, times):
        record = [0] * 60 # there are 0 ~ 59 possible remainders
        result = 0

        for time in times:
            other = 60 - (time % 60)
            # exception here that other can be 60
            if other == 60:
                other = 0
            result += record[other]
            record[time % 60] += 1

        return result
```
