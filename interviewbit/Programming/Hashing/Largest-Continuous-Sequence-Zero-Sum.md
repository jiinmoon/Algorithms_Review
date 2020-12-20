# Largest Continuous Sequence Zero Sum

    Find the largest continuous sequence in a array which sums to zero.

---

## Approach:

We record the prefix sum of values that we have seen thus far; if there exist
same prefix sum already, then we have our candidate sequenece that starts from
previous prefix sum recorded. 

O(n) in both time and space complexity.

---

Python:

```python

class Solution:

    def lcsZeroSum(self, nums):
        
        # guard
        d = { 0 : -1 }

        maxThusFar, l, r, prefixSum = 0, 0, 0, 0

        for i, num in enumerate(nums):
            
            prefixSum += num

            if prefixSum not in d:
                d[prefixSum] = i

            else:
                if maxThusFar < i - d[prefixSum]:
                    maxThusFar = i - d[prefixSum]
                    l = d[prefixSum] + 1
                    r = i
        
        return nums[l:r+1} if maxThusFar else []
```
            


