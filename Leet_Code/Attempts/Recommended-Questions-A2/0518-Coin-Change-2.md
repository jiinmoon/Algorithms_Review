# 518. Coin Change 2

You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that
amount. You may assume that you have infinite number of each kind of coin.

---

We may approach this problem with a dynamic programming.

Let us first prepare an dp array where dp[i] records the total number of ways
to add up to that i amount of money. Then, as we iterate on each given coin,
the dp[i] would be based on the previous number of ways to sum to amount at
dp[i-coin]. In other words, we carry over previous number of ways that we have
formed by adding the coin. So long as amount + coin is greater, we can add
additional.

Suppose we have an amount of 5 and coins of [1, 2, 5].

```

dp = [1, 0, 0, 0, 0, 0]

(1) Coin of 1:

    From 1 to amount of 5, update dp. For coin of 1, there is a single way to
    make to every amount between 1 to 5. 

    dp = [1, 1, 1, 1, 1, 1]

(2) Coin of 2:

    From 2 to amount of 5, update dp. For coin of 2, we can start to increment
    the number of ways starting from 2. Previous values from i - 2 is also
    carried over as it is information from the coin of 1. Notice that for
    i from 4, we can also combine additional ways compute by i - 2.

    dp = [1, 1, 2, 2, 3, 3]
    
(3) Coin of 5:

    From 5 to amonut of 5, update dp. By simple deduction, 5 can only make up
    5. Hence, dp[5] is update as previous sum from dp[0] for additional way.

    dp = [1, 1, 2, 2, 3, 4]

```

Time complexity would be O(m * n) where m is number of coins, and n is the
amount of given money. The space requirement is O(m).

---

Java:

```java

class Solution518 {

    public int change(int amount, int[] coins)
    {
        int[] dp = new int[amount + 1];
        dp[0] = 1;

        for (int coin : coins)
        {
            for (int i = coin; i < amount + 1; i++)
                dp[i] += dp[i-coin];
        }

        return dp[amount];
    }
}

```
