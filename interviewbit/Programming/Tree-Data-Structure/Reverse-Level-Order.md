# Reverse Level Order

    Given a binary tree, return the reverse level order traversal of its nodes
    values. (i.e, from left to right and from last level to starting level).

---

## Approach:

We use BFS to collect the levels of the binary tree; we reverse the ordering as
we do so - using deque data structure or stack.

O(n) in time complexity.

---

Python:

```python

from collections import deque

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        
        if not A:
            return []
            
        queue, result = deque([A]), deque()
        
        while queue:
            
            node = queue.popleft()
            result.appendleft(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
            
        return result
```
