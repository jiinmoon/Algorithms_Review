# 1010. Pairs of Songs With Total Durations Divisible by 60

In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds
is divisible by 60.  Formally, we want the number of indices i, j such that
i < j with (time[i] + time[j]) % 60 == 0.

---

For each of the song duration, we record count of how many seconds leftover
after modulo by 60 - then, we can quickly look up the count by the needed
amount in the record. The time and space complexity should be O(n).

---

```python

class Solution:
    def numPairsDivisibleBy60(self, time):
        # 0 ~ 60 possible seconds needed and their count of songs
        record = [0] * 60
        result = 0
        for t in time:
            neededCounts = 60 - (t % 60)
            if neededCounts == 60:
                neededCounts = 0
            result += record[neededCounts]
            record[t % 60] += 1
        return result
```
