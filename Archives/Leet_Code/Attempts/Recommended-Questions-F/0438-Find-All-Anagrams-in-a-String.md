# 438. Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's
anagrams in s.

Strings consists of lowercase English letters only and the length of both
strings s and p will not be larger than 20,100.

The order of output does not matter.

---

Naive approach would be to iterate on the given string s for every length of
the p; and then check to see whether we have used all the counts of the
characters from the p. This would be O(n^2) in time complexity as we have to
find all substring length equal to length of p and then check the membership of
the characters.

To improve upon this, we use sliding window. First, we create a hashmap that
tracks the count of the characters found within the p. So, as we iterate on the
given string s, we update the hashmap by removing the first element in the
sliding window (s[i]) and adding the last element which is the s[i+len(p)].
Once the hashmap count is empty, we have no more characters left in the pool,
so we can add current index as the start of the sliding window of size len(p)
in string s that shares same anagrams.

The time complexity should be O(n) where n is the length of the string
s.

---

Python:

```python

class Solution:
    def findAnagrams(self, s, p):
        def update(char, count):
            counter[char] += count
            if not counter[char]:
                counter.pop(char)

        m, n = len(s), len(p)
        if n > m:
            return []

        counter = collections.defaultdict(int)
        result = list()

        for char1, char2 in zip(p, s[:n]):
            update(char1, -1)
            update(char2, 1)

        for i in range(m - n):
            if not counter:
                result.append(i)
            update(s[i], -1)
            update(s[i+n], 1)

        if not counter:
            result.append(m - n)
        return result
```
