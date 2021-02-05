# 1520. Maximum Number of Non-overlapping Substrings

Given a string s of lowercase letters, you need to find the maximum number of
non-empty substrings of s that meet the following conditions:

The substrings do not overlap, that is for any two substrings s[i..j] and
s[k..l], either j < k or i > l is true.
A substring that contains a certain character c must also contain all
occurrences of c.
Find the maximum number of substrings that meet the above conditions. If there
are multiple solutions with the same number of substrings, return the one with
minimum total length. It can be shown that there exists a unique solution of
minimum total length.

Notice that you can return the substrings in any order.

---

Let's think of this problem in terms of windows - and finding non-overlapping
ranges. First, we collect all of our possible ranges (left, right) by iterating
over each of the unique characters then finding the leftmost and rightmost
indicies.

Theses will be a starting point to build our candidate windows. For each
character, we update the leftmost index and rightmost index of the window by
checking for every character's recorded min/max occurrences in the substring. 

This candidates can now be sorted by their right indicies; for each candidate,
if their left index is greater than the previous substring's right index, this
is a valid result.

Due to sorting invovled, the complexity should be O(n * log(n)) and O(n) for
space.

---

Python:

```python

class Solution1520:

    def maxNumberSubstrings(self, s):
        if not s:
            return []

        chars = set(s)
        record = {char : (s.index(char), s.rindex(char) + 1) for char in chars}

        candidates = []
        for char in chars:
            minLeft = left = record[char][0]
            maxRight = right = record[char][1]

            while True:
                for c in s[left:right]:
                    left = min(left, record[c][0])
                    right = max(right, record[c][1])
                if left == minLeft and right == maxRight:
                    candidates.add( (left, right) )
                    break
                minLeft, maxRight = left, right
        
        prevRight = 0
        result = []
        for currLeft, currRight in sorted(candidates, key=lambda x : x[1]):
            if currLeft >= prevRight:
                result.append( s[currLeft:currRight] )
                prevRight = currRight

        return result
```
