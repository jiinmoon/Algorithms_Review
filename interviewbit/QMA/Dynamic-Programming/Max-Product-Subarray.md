# Max Product Subarray

Find the contiguous subarray within an array (containing at least one number)
which has the largest product.

Return an integer corresponding to the maximum product possible.

---

Problem is the negative num that can potentially create a local max contiguous
subarray. Hence, we maintain both maxPostive and maxNegative contiguous
products and find the maximum.

O(n) in time complxity.

---

Python:

```python

class Solution:

    def maxProductSubarray(self, nums):

        minNeg, maxPos, result = 1, 1, float('-inf')

        for num in nums:
            temp = maxPos
            maxPos = max(num, max(maxPos * num, minNeg * num))
            minNeg = min(num, min(temp * num, minNeg * num))

            result = max(result, maxPos)

        return result
```


