114 Flatten BInary Tree to Linked List
======================================

Question:
---------

Given a binary tree, flatten it to a linked list where every node only has
a right child.

Solutions:
----------

One approach is we continuously traverse to the right of the binary tree. At
each node, we have following cases:

1. Node has a right child:

In this case, we can continue to traverse on right.

2. Node has a left child:

The left subtree should be reattached to the right and set the left to None.
But we first need to save the right pointer if it exists. Thus, when we check
for the right child in step 1, we should save its pointer to the stack such
that we can revisit.

3. Otherwise, continue traversing on right.

Codes:
------

Python:

```python
class Solution:
    def flatten(self, root):
        stack = []
        while root or stack:
            # case 1
            if root.right:
                stack.append(root.right)
            # case 2
            if rott.left
                root.right = root.left
                root.left = None
            root = stack.pop() if stack else root.right
```

---

**Source:**

LeetCode:
[Flatten-Binary-Tree](https://leetcode.com/problems/flatten-binary-tree-to-linked-list)
