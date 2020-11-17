# 465. Optimal Account Balancing

A group of friends went on holiday and sometimes lent each other money. For
example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5
for a taxi ride. We can model each transaction as a tuple (x, y, z) which means
person x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and
2 respectively (0, 1, 2 are the person's ID), the transactions can be
represented as [[0, 1, 10], [2, 0, 5]].

Given a list of transactions between a group of people, return the minimum
number of transactions required to settle the debt.

---

To deduce the minimum number of transfer of funds between people to balance out
all the outstanding debts amongst them, we keep track of how much money has
been exchanged between two people. If A has lended Z amount to B, we record
Z as B needs to cover Z to A; and vice versa.

Then, all we need to work with is a list of balances that we need to find the
combinations of and repeatedly reduce the balances until we have none left
standing.

Approaching this problem recursively, the base case would be when we have no
outstanding balances to cover. For each balance, we check to see whether there
is a value out there that can immediately cancel out to 0, which is the most
optimal case. We recursively explore down this path incrementing the count of
transfer and reduce the used balance to cancel out. Otherwise, we exhaustively
search downward, checking against every other balance that can hopefully reduce
it further.

The time complexity would be O(m + n!) where m is the number of transfers
occured between people, and n is the number of people. This is since we have to
spend m time to build our balances to cover; and n! to explore all possible
options to reduce our balances.

---

Python:

```python

class Solution:
    def minTransfers(self, transactions):
        # (A, B, Z) means A lended B, Z amount
        # also means B owes A, Z amount
        transfers = collections.defaultdict(int)
        for A, B, Z in transactions:
            transfers[A] += Z # A lended Z
            transfers[B] -= Z # B owed Z

        toBalance = [amount for amount in transfers.values() if amount]

        def helper(toBalance):
            # base case: all outstanding balances are cancel'd
            if not toBalance:
                return 0

            curr = toBalance[0]

            # best case: another balance can cancel out current exactly
            for i in range(1, len(toBalance)):
                if curr - toBalance[i] == 0:
                    # remove ideal balance and recursively explore downwards
                    return 1 + helper(toBalance[1:i] + toBalance[i+1:])

            # otherwise, exhaustively search all cases if it can reduce
            minThusFar = float('inf')
            for i in range(1, len(toBalance)):
                if curr * toBalance[i] < 0:
                    # append the remaining amount to balance in the end!
                    depth = 1 + helper(toBalance[1:i] + toBalance[i+1:] + [curr + toBalance[i]])
                    minThusFar = min(minThusFar, depth)

            return minThusFar

        return helper(toBalance)
```
