# 987. Vertical order Traversal of a Binary Tree

Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will
be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the
vertical line touches some nodes, we report the values of the nodes in order
from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is
reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report
will have a list of values of nodes.

---

Starting from the root which is marked as (0, 0), we traverse while updating
each coordinates. When we move down, y - 1. When we move to left child,
x - 1 and vice versa on the right child. Since we want to find the ordering
first based on x, we create a record where we will have all x coordinates as
keys and its values will be the list of tuple of depth (y) and nodes. Then,
once we finished traversing on the binary tree, we can sort the record first by
its key (x) to retrieve the order based on x. Then, on the given list of
y coords to nodes, we sort again to retrieve the value of nodes from top to
bottom. Since the sorting is involved, the time complexity would be O(n
* log(n)) - we have to sort for each x coords the list of y coords, but these
  are guranteed to be less than count of x.

---

Python:

```python

class Solution:
    def verticalTraversal(self, root):
        def helper(node, x, y):
            if not node:
                return
            # negate y to get top to bottom decreasing order
            coordMap[x].append((-y, node.val))
            helper(node.left, x-1, y-1)
            helper(node.right, x+1, y-1)

        coordMap = collections.defaultdict(list)
        helper(root, 0, 0)

        result = list()
        for x in sorted(coordMap.keys()):
            coordMap[x].sort()
            result.append([val for _, val in coordMap[x]])
        return result
```
