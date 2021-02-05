# 1239 Maximum Length of a Concatenated String with Unique Characters

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be
separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between
two words. The returned string should only have a single space separating the
words. Do not include any extra spaces.

---

To solve this problem, we utilize the set data structure to identify the unique
characters. Firstable, we create a set of character sets from a given list of
strings iff the string itself consists of unique characters.

Then, we have a result of sets to be updated. For each of the unique character
set created in the beginning, we iterate on the sets within the result. We "OR"
the two character sets; if the concatenated character set created only contains
the unique characters, then it is included for the next set of result.

---

Python:

```python

class Solution:
    def maxLength(self, arr):
        charSets = [set(s) for s in arr if len(set(s)) == len(s)]
        result = [set()]

        for currSet in charSets:
            for prevSet in result.copy():
                newSet = currSet | prevSet
                if len(newSet) == len(currSet) + len(prevSet):
                    result.append(newSet)

        return max(result, key=len)
```
