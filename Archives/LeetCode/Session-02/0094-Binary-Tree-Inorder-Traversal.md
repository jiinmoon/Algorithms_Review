# 94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes'
values.

---

Recursive solution is rather trivial; hence, iterative approach would be much
more interesting for discussion here. For inorder traversal in iterative
implementation, we must remember that we have to revisit the nodes as we
traverse to the leftmost nodes from each of the node. Upon second revisit to
the node, we can record that node's value and check to see whether its right
subtree exist - in which case, repeats the process until we explore all of the
subtree.

---

Python: Iterative approach.

```python

class Solution94:

    def inorderTraversal(self, root):

        stack, result = [], []

        while root or stack:
            
            # find leftmost node while saving previous visited node
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            # every node here on is the revisit;
            # hence, record current node and check right subtree to repeat the process
            
            if root:
                result.append(root.val)
                root = root.right

        return result
```
