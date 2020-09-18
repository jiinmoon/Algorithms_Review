340 Longest Substring with At Most K Distinct Characters
========================================================

Given a string, find the length of the longest substring T that contains at
most k distinct characters.

---

A naive approach requires a hashset which will record the characters that we
have seen previously. For each character, we expand as far as possible with
hashset to check for the duplication. This will be O(n^2) in time complexity.

A better approach would be to utilize the sliding window. We maintain the last
index of each character and continuously add new character until we have
k distinct characters; if exceeding k, we start to move our window forward from
left. This would be O(n) in time complexity.

---

Python:

```python

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # { char : last index seen from curr position }
        lastIndex = collections.defaultdict(int)
        srt, longest = 0, 0

        for end, char in enumerate(s):
            lastIndex[char] = end

            # there are more than k distinct between [srt:end]
            # move start forward while updating lastIndex
            while len(lastIndex) > k:
                if lastIndex[s[srt]] == srt:
                    lastIndex.pop(s[srt])
                srt += 1
            # if not updated, then current window is valid.
            else:
                longest = max(longest, end - srt + 1)

        return longest
```
