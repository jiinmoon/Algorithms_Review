# 121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.

---

To find the maximum profit, we simply iterate forward to simulate the "buying"
a stock and "selling" a stock. Intuitively, the maximum profit can be made by
"buying" when the stock is low and "selling" when it is high.

Hence, for each price that we examine, we check to see whether it is worth
"buying" at its current price - that is, it is the minimum of the what we have
seen thus far. To find the maximum profit, we then simply try to see whether
selling what we have bought previous (minimum price found previously) to
current price.

Overall, the time complexity should be linear.

---

Python:

```python

class Solution121:

    def maxProfit(self, prices):

        buy, sell = float('inf'), 0

        for price in prices:
            buy = min(buy, price)
            sell = max(sell, price - buy)

        return sell
```
