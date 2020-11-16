# 22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

---

We may generate all combinations of well-formed parentheses by maintaining the
count of open parentheses that we have added to our path thus far as well as
the number of pairs still needed to be added.

At each recursive call, we check whether we have no more open parentheses to
close as well as no more pairs to add. This base case signals we have
a candidate path that can be added to our result. Otherwise, we should check
for whether there are any open parentheses added previously that should be
closed, in which case we recursively call to explore down the path by appending
the closing parenthesis. And we check to see whether there are more pairs of
parentheses to add, in whcih case we recursively call by expanding path with an
open parenthesis.

At each case, there are two options to explore, hence the time complexity would
be O(2^n).

---

Python:

```python

class Solution:
    def generate(self, n):
        def helper(path, openCount, pairCount):
            if not openCount and not pairCount:
                result.append(path)
                return
            if openCount:
                helper(path + ")", openCount - 1, pairCount)
            if pairCount:
                helper(path + "(", openCount + 1, pairCount - 1)

        result = list()
        helper("", 0, n)

        return result
```


