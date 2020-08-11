# LeetCode Daily Challenge: August Week.2 - Day.4

## Question

Given an array of citations (each citation is a non-negative integer) of
a researcher, write a function to compute the researcher's h-index.

A scientist has indexh if h of his N papers have at least h citations each, and
the other N - h papers have no more than h citations each.

## Solution

We will first sort the papers by its number of citations. Then, we will iterate
on the papers from the most citations, adding them to the cumulative sum and
until there are at least as many papers as citations.

Python:

```python
class Solution:
    def hIndex(self, citations):
        m = len(citations)
        buckets = [0] * (m+1)
        for c in citations:
            # sort by number of citations.
            # buckets[i] == number of papers cited i times.
            buckets[min(c, m)] += 1
        
        # count the papers with at least buckets citations.
        papers = 0
        for bucket in range(len(buckets)-1, -1, -1):
            papers += buckets[bucket]
            if papers >= bucket:
                return bucket
```

