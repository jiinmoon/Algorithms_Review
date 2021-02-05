# Least Common Ancestor

    Find the lowest common ancestor in an unordered binary tree given two values in
    the tree.

    Lowest common ancestor : the lowest common ancestor (LCA) of two nodes v and
    w in a tree or directed acyclic graph (DAG) is the lowest (i.e. deepest) node
    that has both v and w as descendants. 


    You are given 2 values. Find the lowest common ancestor of the two nodes
    represented by val1 and val2

    No guarantee that val1 and val2 exist in the tree. If one value doesn’t exist
    in the tree then return -1.

    There are no duplicate values.

    You can use extra memory, helper functions, and can modify the node struct but,
    you can’t add a parent pointer.

---

## Approach:

The problem here is that there is no gurantee that two values may not exist.
Hence, when we recursively traverse down while searching for LCA, we have to
check whether the two values have been found or not. So, we use flags to denote
whether the two values have been found.

O(n) in time complexity.

---

Python:

```python
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        
        found = 0
        
        def helper(node):
            nonlocal found
            
            if not node:
                return None
                
            l, r = helper(node.left), helper(node.right)
            
            # left and right subtree found targets; return current root
            if l and r:
                return node
                
            # found target nodes; set flag
            if node.val in { B, C }:
                found += (node.val == B and node.val == C) + 1
                return node
            
            return l or r
        
        result = helper(A)
        
        return result.val if result and found == 2 else -1
```
