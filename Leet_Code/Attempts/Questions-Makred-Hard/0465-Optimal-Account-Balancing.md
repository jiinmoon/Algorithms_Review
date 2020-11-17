# 465. Optimal Account Balancing

A group of friends went on holiday and sometimes lent each other money. For
example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5
for a taxi ride. We can model each transaction as a tuple (x, y, z) which
means person x gave person y $z. Assuming Alice, Bill, and Chris are person 0,
1, and 2 respectively (0, 1, 2 are the person's ID), the transactions can be
represented as [[0, 1, 10], [2, 0, 5]].

Given a list of transactions between a group of people, return the minimum
number of transactions required to settle the debt.

---

Given list of transactions (A, B, C), we determine that A has lended B an
amount of C. This means that C amount of balance needs to be negated out.
Hence, for each transactions made, we create a list of balances that needs to
be balanced out to zero.

Using recursion, at each depth, we try to balance out the very first balance.
The most optimal case would be there is some other balance out there that can
completely null out the current balance. In this case, the result would simply
be 1 transaction + whichever amount to follow for the remainder of the
balances.

Otherwise, we start exhuastive trying of every balances that can be use to
reduce the current balance further out.

The time complexity would be O(n!) where n are the number of people as at worst
case, we have to consider every possible combinations of balances to consider.

---

Python:

```python

class Solution:
    def optimalTransactions(self, transactions):
        g = collections.defaultdict(int)
        # A lends to B $Z amount of money
        # A -> B is positive balance to negate out
        # B -> A is negative balance to positive out
        for A, B, val in transactions:
            g[A] += val
            g[B] -= val
        
        # only relavent balances are those non-zero ones
        # they are used to balance each other out
        balances = [b for b in balances if b]

        def helper(balances):
            if not balances:
                return 0
            
            # current balance to zero out
            curr = balances[0]

            # most optimal case; balances completely to zero
            for i in range(1, len(balances)):
                if curr + balances[i] == 0:
                    return 1 + helper(balances[1:i] + balances[i+1:])

            # otherwise, exhaustively try all others that reduces the balance
            minTransferAmount = float('inf')
            for i in range(1, len(balances)):
                # if either is negative, we can reduce it
                if (curr < 0) ^ (balances[i] < 0):
                    # remeber to append remainder after reducing it
                    currTransferAmount = 1 + helper(balances[1:i] + balances[i+1:] + [curr + balances[i]])
                    minTransferAmount = min(minTransferAmount, currTransferAmount)

            return minTransferAmount

        return helper(balances)
```


