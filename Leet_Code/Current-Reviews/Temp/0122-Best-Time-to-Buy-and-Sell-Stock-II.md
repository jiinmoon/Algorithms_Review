# 122. Best Time to Buy and Sell Stock II

Say you have an array prices for which the ith element is the price of a given
stock on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (i.e., buy one and sell one share of the stock
multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you
must sell the stock before you buy again).

---

Unlimited number of transactions (or more than half the length of the given
prices) implies that we are to seek maximum sum of differences made between
previous and current prices. O(n) in time complexity.

---

Java:

```java

class Solution122 {

    public int maxProfit(int[] prices)
    {
        int result = 0;

        for (int i = 1; i < prices.length; i++)
            if (prices[i] > prices[i-1])
                result += prices[i] - prices[i-1];

        return result;
    }
}

```

