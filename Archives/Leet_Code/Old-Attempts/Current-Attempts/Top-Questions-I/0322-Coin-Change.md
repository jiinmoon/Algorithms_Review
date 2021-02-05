# 322 Coin Change

You are given coins of different denominations and a total amount of money
amount. Write a function to compute the fewest number of coins that you need to
make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

---

We may approach this problem as a binary tree of different coin combinations
that we can explore. At each depth, we try to remove the largest possible coins
until we reach the goal of 0 amount. If not possible, then we move onto the
next possible coin combination. O(n^d) time complexity where n is the number of
the coins and d is the depth of the tree (total amount / smallest possible
coin).

---

Python:

```python

class Solution:
    def coinChange(self, coins, amount):
        def helper(remaining, currCoin, usedCoin):
            # goal is reached
            # it is a possible combination that can be recorded
            if not remaining:
                self.result = min(self.result, usedCoin)
             
            for i in range(currCoin, len(coins)):
                # early exist - result cannot be improved
                if remaining >= coins[i] * (self.result - usedCoin):
                    break
                # we can still take away current coin amount from remaining
                if coins[i] <= remaining:
                    helper(remaining - coins[i], i, usedCoin + 1)
        
        # use largest coin first
        coins.sort(reversed=True)
        self.result = float("inf")
        helper(amount, 0, 0)

        return self.result if self.result != float("inf") else -1
```
