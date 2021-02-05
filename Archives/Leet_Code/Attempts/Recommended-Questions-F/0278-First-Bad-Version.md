# 278. First Bad Version

You are a product manager and currently leading a team to develop a new
product. Unfortunately, the latest version of your product fails the quality
check. Since each version is developed based on the previous version, all the
versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first
bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version
is bad. Implement a function to find the first bad version. You should minimize
the number of calls to the API.

---

This is essentially a binary search problem where we are trying to find the
leftmost version that is marked as bad by the API call to the isBadVersion.
Hence, the time complexity of this algorithm should be O(log(n)).

---

Python:

```python

class Solution:
    def firstBadVersion(self, n):
        l, r = 1, n # starts from 1 to n
        while l < r:
            mid = l + (r - l) // 2
            # keep reduce to left
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l
```
