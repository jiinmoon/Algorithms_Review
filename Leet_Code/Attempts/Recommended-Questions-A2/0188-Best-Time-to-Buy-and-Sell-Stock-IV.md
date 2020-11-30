# 188. Best Time to Buy and Sell Stock IV

You are given an integer array prices where prices[i] is the price of a given
stock on the ith day.

Design an algorithm to find the maximum profit. You may complete at most
k transactions.

Notice that you may not engage in multiple transactions simultaneously (i.e.,
you must sell the stock before you buy again).

---

Here, we first note that if we can complete k number of transactions where k is
half of the given prices length, then it is a simple sum of all the differences
as we can complete transations every single day - so long as the difference is
the net positive.

Extending this approach, we may use dynammic programming: upto i-th point,
current max profit that we can make per each transaction would be either the
maximum of previous transactions' at i-th point, or current max profit found
thus far plus the current difference. Then, dp at i (max profit upto i) would
be either maximum of previous max profit (max profit upto i - 1) or current
maximum that we have found.

Hence, for number of transactions, we repeatedly examine and update our dp for
every prices considered.

---

Java:

```java

class Solution188 {

    public int maxProfit(int[] prices, int k)
    {
        if (k >= (prices.length / 2))
        {
            int result = 0;
            for (int i = 1; i < prices.length; i++)
                result += Math.max(0, prices[i-1] - prices[i]);
            return result;
        }
        
        int[] dp = new int[prices.length];
        
        while (k-- > 0)
        {
            // repeat finding maximum profit upto k transactions
            int currMaxProfit = 0;
            for (int i = 1; i < prices.length; i++)
            {
                // max profit upto this point is previous max profit upto i, or
                // current max profit that we have found plus current differences in price
                currMaxProfit = Math.max(dp[i], currMaxProfit + prices[i-1] - prices[i]);
                // record possible new max profit found thus far
                // max profit upto i is previous at i-1 or current new max profit found
                dp[i] = Math.max(dp[i-1], currMaxProfit);
            }
        }

        return dp[dp.length-1];
    }
}

```
