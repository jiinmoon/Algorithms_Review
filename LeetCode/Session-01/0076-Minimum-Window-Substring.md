# 76. Minimum Window Substring

Given two strings s and t, return the minimum window in s which will contain
all the characters in t. If there is no such window in s that covers all
characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be
only one unique minimum window in s.

---

Here, we use hashmap to record current substring characters. Also, we use
integer variable to denote how many more number of characters are there left to
match.

As we iterate forward, we check to see whether our current substring has more
characters to match up. If so, then we extend our substring window by appending
last character (record it onto our hashmap). Otherwise, our current substring
is a potential candidate for minimum window substring. We record its length,
and shrink the size of substring in the front while updating the hashmap at the
same time.

This would be O(s) in time complexity and space complexity.

---

Python:

```python

from collections import Counter

class Solution76:

    def minWindowSubstring(self, s, t):
        
        # we need to cover all characters in t
        counter = Counter(t)
        
        # current substring window start and end positions
        start, end = 0, -1
        # resulting minimum substring window
        minStart, minEnd = 0, float('inf')
        match = len(t)

        while end < len(s) - 1 or match == 0:
            # still more characters to cover until all characters in t matches
            if match:
                end += 1
                if s[end] in counter:
                    count[s[end]] -= 1
                    if counter[s[end]] >= 0:
                        match -= 1
            # current window matched all characters in t
            else:
                if minEnd - minStart >  end - start:
                    minStart = start
                    minEnd = end

                # shirnk the current window from start
                # return character back to the pool to be matched
                if s[start] in counter:
                    counter[s[start]] += 1
                    if counter[s[start]] > 0:
                        match += 1
                start += 1
        
        if minEnd == float('inf'):
            return ""

        return s[minStart:minEnd + 1]
```
