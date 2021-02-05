# 322. Coin Change

You are given coins of different denominations and a total amount of money
amount. Write a function to compute the fewest number of coins that you need to
make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

---

Let's approach this problem as a DP:

    Define DP[i] as a minimum amount of coins that would make up to i.

    Then, DP[i] can be built by for every coin that we examine, we iterate upto
    every value that we can make using that coin.

    Either DP[i] stays the same, or carries over previous (value - coin)
    \+ 1 for current coin used.

        DP[i] = min(DP[i], DP[val - coin] + 1)

O(c * n) for time complexity as we have to iterate upto n amount for every coin
c. O(n) for space complexity to maintain DP array.

---

Python:

```python

class Solution322:

    def coinChange(self, coins, amount):

        dp = [float('inf') for _ in range(amount + 1)]
        
        for coin in coins:
            for val in range(coin, amount + 1):
                dp[val] = min(dp[val], dp[val - coin] + 1)
        
        return dp[-1] if dp[-1] != float('inf') else -1
```
