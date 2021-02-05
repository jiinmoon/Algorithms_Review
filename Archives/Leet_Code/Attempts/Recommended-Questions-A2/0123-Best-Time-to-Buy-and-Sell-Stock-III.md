# 123. Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete at most two
transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you
must sell the stock before you buy again).

---

This is an extension from the previous question 121. Here, we simply maintain
further second minimum price that we have seen thus far, and record the maximum
profit to be made after selling that second minimum price.

---

Python:

```python

class Solution123:

    def maxProfit(self, prices):
        minBuy1 = minBuy2 = float('inf')
        maxSell1 = maxSell2 = 0

        for price in prices:
            minBuy1 = min(minBuy1, price)
            maxSell1 = max(maxSell1, price - minBuy1)
            minBuy2 = min(minBuy2, price - maxSell1)
            maxSell2 = max(maxSell2, price - minBuy2)

        return maxSell2
```
