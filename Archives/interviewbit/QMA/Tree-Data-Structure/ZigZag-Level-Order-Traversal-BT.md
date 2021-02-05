# ZigZag Level Order Traversal BT

Given a binary tree, return the zigzag level order traversal of its nodes’
values. (ie, from left to right, then right to left for the next level and
alternate between).

---

We can use BFS to traverse the tree in level order fashion - at each level, we
flip the ordering and add to our result. O(n) in time complexity.

---

Python:

```python

class Solution:

    def zigzagLevelOrder(self, root):

        if not root:
            return []

        result, queue, flip = [], [root], False

        while queue:

            if flip:
                result.append([n.val for n in queue[::-1])
            else:
                result.append([n.val for n in queue])

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
