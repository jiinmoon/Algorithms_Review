# 96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store
values 1 ... n?

---

For each BST tree rooted at i where 1 <= i <= n has left subtree whose values
are between (1, i - 1) and right subtree (i + 1, n). Let's take an example:

```

Suppose n = 6. And now, we are consider 3 as our root of the BST.

Then, left subtree should contain values [1, 2] and right subtree [4, 5, 6].

As for left subtree, we can only make 2 structurally sound tree (one rooted at
1 and other at 2); but for right subtree, we can have upto five which are:

    4                       |               4
        \                   |                   \
            5               |                       6
                \           |                   /
                    6       |               5


            5               |               5
        /       \           |                   \
    4               6       |                       6
                            |                   /
                            |               4


                    6
                /
            5
        /
    4


Thus, for each choice of our root to left, we have 5 choices on right. Thus,
total would be 10 for the root of 3.

```

Hence, we can solve this problem as a recursion with help of memoization: at
each depth, we iterate to consider every value as its current root. Then, total
number of BST that we can have at this root would be product of result found to
its left subtree (i - 1) and right subtree (n - i).

Time complexity would be O(n^2) and space is O(n).

---

Python:

```python

from functools import lru_cache

class Solution96:
    
    @lru_cache(None)
    def numTrees(self, n):

        if n <= 1:
            return 1

        result = 0
        for i in range(1, n + 1):
            # left upto (n - i) and right upto (i - 1)
            result += self.numTrees(i - 1) * self.numTrees(n - i)

        return result

```
