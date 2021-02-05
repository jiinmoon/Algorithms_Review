# Right View of Binary Tree

## Problem Description

    Given a binary tree A of integers. Return an array of integers representing the
    right view of the Binary tree.

    Right view of a Binary Tree: is a set of nodes visible when the tree is visited
    from Right side.



## Problem Constraints

    1 <= Number of nodes in binary tree <= 105
    0 <= node values <= 109


## Input Format

    First and only argument is an pointer to the root of binary tree A.


## Output Format

    Return an integer array denoting the right view of the binary tree A.

---

## Approach:

Simply use BFS and gather nodes in level order fashion. The right most value in
the queue or level would be the right view of the binary tree.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def solve(self, A):

        if not A:
            return []

        queue, result = [A], []

        while queue:

            result.append(queue[-1].val)

            temp = []
            
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            queue = temp

        return result
```
