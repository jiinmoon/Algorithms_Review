# ZigZag Level Order Traversal BT

    Given a binary tree, return the zigzag level order traversal of its nodes’
    values. (ie, from left to right, then right to left for the next level and
    alternate between).

---

## Approach:

Use BFS to traverse in level order fashion; for each level, we add them in
zigzag fashion using boolean flag.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def zigzagLevelOrder(self, root):

        if not root:
            return []

        flip, queue, result = False, [root], []

        while queue:

            if flip:
                result.append([node.val for node in queue[::-1])
            else:
                result.append([node.val for node in queue)

            flip = not flip
            temp = []

            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            queue = temp

        return result
```

