121 Best Time to Buy and Sell Stock
===================================

Say you have an array for which the ith element is the price of a given stock on
day i.

If you were only permitted to complete at most one transaction (i.e., buy one
and sell one share of the stock), design an algorithm to find the maximum
profit.

Note that you cannot sell a stock before you buy one.

Example 1:

```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit
= 6-1 = 5. Not 7-1 = 6, as selling price needs to be larger than buying price.
```

Example 2:

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

---

The problem is about finding the minimum price to buy followed by a maximum
price to sell. To do so, we will maintain two variables: "buy" for maximum
balance after buying a stock and "sell" for maximum profit after selling
a stock.

As we iterate on the given stocks, we will simulate buying and selling. The
"buy" is updated as negative - since we will be losing money after buying. When
we "sell", it is updated as either current stock price + previous minimum stock
that we "bought" - or it stays the same.

---

Go:

```go
func maxProfit(prices []int) int {
    var (
        b = -1 << 31
        s = 0
    )
    for _, p := range prices {
        b = max(-p, b)
        s = max(p + b, s)
    }
    return s
}

func max(x, y int) int {
    if x >= y {
        return x
    }
    return y
}
```

