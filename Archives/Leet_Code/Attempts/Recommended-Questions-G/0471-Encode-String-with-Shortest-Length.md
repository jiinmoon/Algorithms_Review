# 471. Encode String with Shortest Length

Given a non-empty string, encode the string such that its encoded length is the
shortest.

The encoding rule is: k[encoded\_string], where the encoded\_string inside the
square brackets is being repeated exactly k times.

Note:

k will be a positive integer.
If an encoding process does not make the string shorter, then do not encode it.
If there are several solutions, return any of them.

---

Using recursion, we explore all possible ways that we can encode the string at
each locations.

For each location, we consider every possible prefix. There are multiple
possibilities when we are considering them:

(1) prefix is found to be repetition. If the current prefix is a possible
repetition, then we can confirm it by concatenating the two strings. If there
is an overlap, the prefix should not be found.

i.e. Considering "aaaaa". Concatenated string would be "aaaaaaaaaa" and finding
the original string "aaaaa" from index 1 and on should return 1 since starting
from index 1, we find the matching substring. Thus, repetition is found.

i.e. Another example "aabcaabc" will find index 4 as repetition. So, we
compress it to "2[aabc]".

If so, then our current result can be saved as a potential compressed string.
We compress the string upto index found above, and then for the remaining
string we recursively find further possible compressions down the path.

(2) there does not exist any repetition. In such case, we have to break down
each position and recursively find compressions to prefix and suffixes.

Once we have gathered all the compressed strings from the paths, we find the
minimum amongst them.

As there is a single possible minimum compressed string found on each depth and
for specific break point, we may use memoization.

Due to having to explore all possible prefix and suffixes for compressions,
this recursive process would have time complexity of O(n**3).

---

Python:

```python

from functools import lru_cache

class Solution:
    def encode(self, s):
        @lru_cache(None)
        def helper(s):
            # gather all possible compression on s
            result = [s]

            # find where repetition occurs
            i = (s + s).find(s, 1)
            # if found, compress and explore downwards
            if i != -1 and i != len(s):
                result.append(
                    str(len(s)//i) + "[" + helper(s[i:]) + "]"
                )

            # otherwise, explore all prefix and suffix
            for i in range(1, len(s)):
                prefix = s[:i]
                suffix = s[i:]
                result.append(
                    helper(prefix) + helper(suffix)
                )

            # finished exploring thus far; find min from this
            result = min(result, key=len)
            return result

        return helper(s)
```


