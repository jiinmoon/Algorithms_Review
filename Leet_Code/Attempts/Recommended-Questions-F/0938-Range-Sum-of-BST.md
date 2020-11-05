# 938. Range Sum of BST

Given the root node of a binary search tree, return the sum of values of all
nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

---

One simple approach to this problem would be to perform inorder traversal on
the given BST. This will retrieve the ordered list of integers which we can
find the positions of L and R to sum them up to return. This would cost us an
additional space to record the values as we iterate on the given BST.

Another approach would be to use recursion to add up the values as we traverse
on the tree to left and right. At each node, we would first check to see
whether current node value is within the range: if the current node value is
greater than R, we return the recursive call to node's left and vice versa. If
we determine that the current node indeed is within the range, then we can
return the value of sum of current node.val and values returned from the tree's
left and right. This would be O(n) in both time and space.

---

Python:

```python

class Solution:
    def rangeSumBST(self, root, L, R):
        if not root: return 0
        if root.val > R: return self.rangeSumBST(root.left, L, R)
        if root.val < L: return self.rangeSumBST(root.right, L, R)
        return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
```
