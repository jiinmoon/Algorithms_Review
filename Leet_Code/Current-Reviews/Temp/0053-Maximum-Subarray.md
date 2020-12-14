# 53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another
solution using the divide and conquer approach, which is more subtle.

---

#### (1) Iterative greedy aproach.

Simple solution would be to use greed algorithm. Here, we have cumulative local
sums of the contiguous subarray determined by breaking off when we discover
that current element does not increase our sum. Amongst these, we are trying to
pick the maximum. Time complexity would be O(n) and space complexity would be
O(1).

#### (2) DP.

Another solution would be to define our DP at i-th index as a maximum
contiguous subarray sum that we have seen thus far. Hence, so long as the
previous value can increase the sum, we can add to our current dp at i. Amongst
these, we choose the maximum. Time complexity would be linear. Space complexity
depends upon whether we can modify the given array - if so, then it would be
O(1).

---

Python: greedy algorithm.

```python

class Solution53:

    def maxSubArray(self, nums):

        if not nums:
            return 0

        currSum, maxSum = 0, float('-inf')

        for num in nums:
            # current sum can extend iff current num can increase it
            currSum = max(currSum + num, num)
            maxSum = max(currSum, maxSum)

        return maxSum
```

Python: DP approach.

```python

class Solution53:

    def maxSubArray(self, nums):
        
        if not nums:
            return 0

        maxSum = nums[0]

        for i in range(1, len(nums)):
            # so long as it can increase it, we include to current
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            maxSum = max(maxSum, nums[i])

        return maxSum
```

