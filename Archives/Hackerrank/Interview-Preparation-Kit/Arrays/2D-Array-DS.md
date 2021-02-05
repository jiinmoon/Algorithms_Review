2D Array DS
===========

To find the maximum sum of all the hourglasses, we simply iterate on the 2D
array and find all the hourglasses while maintaining the maximum sum.

---

Python:

```python
def hourglassSum(arr):
    if not arr or not arr[0]:
        return 0
    maxSum = float('-inf')
    m, n = len(arr), len(arr[0])

    def hourglass(i, j):
        currSum = 0
        currSum += sum(arr[i][j:j+3)    # top
        currSum += sum(arr[i+2][j:j+3]) # bottom
        currSum += arr[i+1][j+1]        # mid
        return currSum

    for i in range(m-2):
        for j in range(n-2):
            maxSum = max(maxSum, hourglass(i, j))
    return maxSum
```
