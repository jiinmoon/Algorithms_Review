# 3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating
characters.

---

In order to find the longest substring that does not contain duplicates, we
could naively try to examine all substrings from length 2 to check for the
repeatition of the character. But this requires an exhaustive, nested loop that
results in undesriable time complexity.

Instead, we can look to trade off our space to potentially improve our time
complexity. In this instance, we can use hashmap to record the position of the
characters that we have examined thus far and record the last position that we
have seen such a character. Hence, for every new position in the string that we
are examining, we can consider it as either an extension of the currently
on-going substring without the repeat, or if duplicate is found, we simply
update the hashmap with the lastest position of the duplicated entry, and
truncate our substring by the last position of that duplciated character.

By doing so, the time complexity would be linear, but also will require O(n) in
space complexity as well. Further examination will show that since there are
limited number of characters, the space complexity would actually be constant
O(1).

---

Python:

```python

class Solution3:

    def longestSubstrWithoutRepeat(self, s):

        d = dict()
        start, longest = 0, 0

        for end, char in enumerate(s):
            start = max(start, d.get(char, 0))
            d[char] = end + 1
            longest = max(longest, end - start + 1)

        return longest
```


