# 314. Binary Tree Vertical Order Traversal

Given a binary tree, return the vertical order traversal of its nodes' values.
(ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to
right.

---

We can use BFS algorithm to traverse on the given binary tree to visit each
nodes. For each of the nodes that we visit, we will record the node's value as
well as its column. Whenever we move to left child, we mark its col - 1, and
vice versa for the right child. We would need to sort the record to order the
retrieved nodes based on the columns. However, since the number of columns in
the binary tree is bounded by the depth and number of nodes, the overall time
complexity should be O(n).

---

Python:

```python

class Solution:
    def verticalOrder(self, root):
        if not root:
            return []
        
        # maintain node and its col
        q = [(root, 0)]
        record = collections.defaultdict(list)

        while q:
            temp = list()
            for node, col in q:
                if not node:
                    continue
                # record each node that shares same column
                record[col].append(node.val)
                temp.append((node.left, col-1))
                temp.append((node.right, col+1))
            q = temp
        
        # sort by column
        return [record[col] for col in sorted(record.keys())]
```
