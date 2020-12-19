# 2-Sum BInary Tree

    Given a binary search tree T, where each node contains a positive integer, and
    an integer K, you have to find whether or not there exist two different nodes
    A and B such that A.value + B.value = K.

    Return 1 to denote that two such nodes exist. Return 0, otherwise.

- Notes:


    Your solution should run in linear time and not take memory more than O(height of T).
    Assume all values in BST are distinct.


## Approach:

Use hashmap or set data structure to store each value of the nodes that we
visit. If we can find the other value (target - node.value) in the hashmap,
there exists 2 nodes.

O(n) in time and space complexity.

---

Python:

```python

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    
    def t2Sum(self, root, k):
        
        def helper(node, target):
            if not node:
                return False
            if target - node.val in d:
                return True
            else:
                d[node.val] = target - node.val
            return helper(node.left, target) or helper(node.right, target)
        
        d = dict()
        
        return 1 if helper(root, k) else 0
```

