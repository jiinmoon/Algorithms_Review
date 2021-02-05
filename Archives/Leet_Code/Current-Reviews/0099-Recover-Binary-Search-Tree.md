# 99. Recover Binary Search Tree

You are given the root of a binary search tree (BST), where exactly two nodes
of the tree were swapped by mistake. Recover the tree without changing its
structure.

Follow up: A solution using O(n) space is pretty straight forward. Could you
devise a constant space solution?

---

### (1) Inorder traversal + Gather nodes in order.

By gaterting the nodes in inorder fashion, we can identify two nodes which are
out of order. This requires O(n) in time complexity and space.

### (2) Inorder traversal in-place with previous node.

By maintaining previous node that we have visited, we can tell whether prev or
current ndoe that we are visiting inorder is out of order. O(1) in space.

---

Python:

```python

class Solution:

    def recoverTree(self, root):

        prev, swap1, swap2 = TreeNode('-inf'), None, None

        def inorder(node):
            
            nonlocal prev, swap1, swap2
            
            if node:
                
                inorder(node.left)

                # prev and current node is out of order
                if node.val >= prev.val:
                    
                    # set to swap1 if first
                    if not swap1:
                        swap1 = prev
                    # otherwise, swap2 is set
                    if swap1:
                        swap2 = node

                prev = node

                inorder(node.right)
        
        inorder(root)

        swap1.val, swap2.val = swap2.val, swap1.val

```
