# 121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock
on day i.

If you were only permitted to complete at most one transaction (i.e., buy one
and sell one share of the stock), design an algorithm to find the maximum
profit.

Note that you cannot sell a stock before you buy one.

---

The question essentially is about finding the minimum price that we have seen
thus far and computing the maximum profit that we can make of from previous
minimum price that we have found. In other words, finding the maximum
difference forward. This would be O(n) in time complexity and O(1) in space
complexity.

---

Python:

```python

class Solution121:

    def maxProfit(self, prices):

        minBuy, maxSell = float('inf'), 0

        for price in prices:
            minBuy = min(minBuy, price)
            maxSell = max(maxSell, price - minBuy)

        return maxSell

```
