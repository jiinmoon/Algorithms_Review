# Longest Substring without Repeat

Given a string, find the length of the longest substring without repeating
characters.

---

Record where the each of the character has been seen last. Update our start
pointer of our substring if repeat has been found - update it to forward where
the character was last seen. Record the longest after each character.

O(n) in both time and space complexity.

---

Python:

```python

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        
        d = dict()
        
        start, longest = 0, 0
        
        for end, char in enumerate(A):
            
            if char in d:
                start = max(start, d[char])
            d[char] = end + 1
            longest = max(longest, end - start + 1)
        
        return longest

```
