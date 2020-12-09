# 123. Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete at most two
transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you
must sell the stock before you buy again).

---

We can think of this problem as a expansion on the first problem where we could
complete a single transaction - but now, we can complete two with limit that
you cannot buy again before selling previous transaction.

Then, the problem becomes completing two (buy low, and sell high) strategy.
First, we try to find the minimum price and maximum obtainable by selling the
minimum price found thus far. But also, we have to complete additional buying
and selling to compute further maximum. This second buy and selling can be
thought of reinvesting our capital after completing the first transaction.

This would be O(n) in time complexity.

---

Python:

```python

class Solution123:

    def maxProfit(self, prices):

        buy1, buy2 = float('inf'), float('inf')
        sell1, sell2 = 0 ,0

        for price in prices:

            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)

            # reinvesting; minimum price after completing first
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)
        
        return sell2

```


