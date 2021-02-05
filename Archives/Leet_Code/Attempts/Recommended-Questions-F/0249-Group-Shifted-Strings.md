# 249. Group Shifted Strings

Given a string, we can "shift" each of its letter to its successive letter, for
example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"

Given a list of non-empty strings which contains only lowercase alphabets,
group all strings that belong to the same shifting sequence.

---

As we iterate on the given string, we shift each of the strings such that these
start at the beginning of the shift at "a". Then, using hashmap as our record,
we record the current "corrected" or "shifted" string and the its corresponding
string to create a list of strings that belong under that same shifted string.
The time and space complexity should both be O(n).

---

Python:

```python

class Solution:
    def groupStrings(self, strings):
        record = collections.defaultdict(list)
        for string in strings:
            shiftCount = ord(s[0]) - ord('a')
            correctedString = "".join(
                [chr((ord(c) - ord('a') - shiftCount)% 26) 
                    for c in string])
            record[correctedString].append(string)
        return record.values()
```
