# 340. Longest Substring with At Most K Distinct Characters

Given a string, find the length of the longest substring T that contains at
most k distinct characters.

---

Here, we use sliding window approach - maintain the indicies of the previous
examined characters that we have encountered thus far. Then, iterate on the
given string, updating the window. Current character index marks the end point
of our window. If the total length of the window exceeds the K, then we have to
shrink our start point - as we shrink the start window, we also update our
window as well. This will be O(n) in time complexity.

---

Python:

```python

class Solution:
    def findLongestSubstringKDistinct(self, s, k):
        i, result = 0, 0
        # maps the indicies of the previously encountered characters
        window = collections.defaultdict(int)

        for j, char in enumerate(s):
            window[char] = j

            # total number of distinct characters in window > k
            while len(window) > k:
                # shrink the i (starting point) while updating
                if window[s[i]] == i:
                    window.pop(s[i])
                i += 1
            # otherwise, update result for current length j - i
            else:
                result = max(result, j - i + 1)

        return result
```
