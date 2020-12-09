# 95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's (binary search
trees) that store values 1 ... n.

---

We can think of this problem as a building a BST with given sorted list of
integers where root of the tree (and every subtree) iterates from 1 to n. To do
so, we can recursively generate from values 1 to n: for each i, we recursively
traverse to left with values from (left, i - 1) and to right with (i + 1,
right). Then, current node at this depth will be i.

Time complexity is O(n^2 * Catalan(n)) where `Catalan(n) = (2n!) / (n + 1)! n!`.

---

Python:

```python

class Solution95:

    def generateTrees(self, n):

        def helper(l, r):
            if l > r:
                return [ None ]

            result = []
            for i in range(l, r + 1):
                leftSubtrees = helper(l, i - 1)
                rightSubtrees = helper(i + 1, r)

                for leftNode in leftSubtrees:
                    for rightNOde in rightSubtrees:
                        currNode = TreeNode(i)
                        currNode.left = leftNode
                        currNode.right = rightNode
                        result.append(currNode)

            return result


        if not n:
            return []

        return helper(1, n)
```
