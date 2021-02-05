# 173. Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be
initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

---

This iterator can be implemented with a inorder traversal on the given tree.
By using stack, we iteratively visit all the way down to the leftmost node on
the given tree during the construction time.

Then, for each next call, we know that the result to be returned should be
placed on the top of the stack. And since the traversal on the BST is not yet
incomplete, we should also explore the "right" side of the current node, yet
again poluating the stack with the nodes from the right subtree until we are
at the leftmost from the rightside again.

This approach will be O(n) in time complexity for both construction and next
call.

---

Python:

```python

class BSTIterator:
    def __init__(self, root):
        self.stk = list()
        while root:
            self.stk.append(root)
            root = root.left

    def hasNext(self):
        return len(self.stk) != 0

    def next(self):
        node = self.stk.pop()
        if node.right:
            curr = node.right
            while curr:
                self.stk.append(curr)
                curr = curr.left
        return node.val
```
