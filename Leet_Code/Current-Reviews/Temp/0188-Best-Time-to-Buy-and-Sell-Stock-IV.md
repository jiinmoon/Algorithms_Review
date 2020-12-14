# 188. Best Time to Buy and Sell Stock IV

You are given an integer array prices where prices[i] is the price of a given
stock on the ith day.

Design an algorithm to find the maximum profit. You may complete at most
k transactions.

Notice that you may not engage in multiple transactions simultaneously (i.e.,
you must sell the stock before you buy again).

---

This is further expansion on the previous questions: we know following:

    If number of transaction can happen once, then we buy at lowest and sell at
    next highest - maximum differnce going forward.

    If number of transaction can happend twice, then we repeat above strategy
    but considering reinvesting the profit made after completing first
    transaction.

    If number of transaction is at minimum half of length of the given stocks,
    then it is all the positive differences made.

Then, for any aribitary number of k transactions, we have to record maximum
profits that can be made after each transactions to repeat the process of
number of transactions that can happen twice.

Thus, let's think of a dynammic programming approach here:

    Let DP[i] be a maximum profit made after i-th stock. Then, it depends upon
    two variables:

        1. maximum profit to be made at this iteration (transaction).
        2. previous maximum profit at DP[i-1]
    
    The first variable, current maximum profit is the maximum profit that we
    can make upto i-th; it depends upon current value at DP[i] (which is the
    previous max profit at i, k-1 transaction), and difference between prices.

In short, we use maximum subarray sum or Kadane's algorithm here. To review:

```python

def maxContiguousSubarraySum(nums):

    currSum, maxSum = float('-inf'), 0
    for num in nums:
        currSum = max(num, currSum + num)
        maxSum = max(maxSum, currSum)

    return maxSum
```

This is repeated on each of the dp index to explore.

Time complexity would be O(k * n) and O(n) in space complexity.

---

Python:

```python

class Solution188:

    def maxProfit(self, prices, k):

        if k >= len(prices) // 2:
            return sum(max(0, prices[i] - prices[i-1]) for i in range(1, len(prices)))

        dp = [0] * len(prices)

        for _ in range(k):
            
            # dp at i stores max profit upto i at this _ transaction
            # Kadane's algorithm
            currMaxProfit = 0
            for i in range(1, len(prices)):
                currMaxProfit = max(dp[i], currMaxProfit + prices[i] - prices[i-1])
                dp[i] = max(dp[i-1], currMaxProfit)

        return dp[-1]
```

