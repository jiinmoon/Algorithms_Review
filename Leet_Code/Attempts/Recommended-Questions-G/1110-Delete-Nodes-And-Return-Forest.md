# 1010. Delete Nodes And Return Forest

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to\_delete, we are left with a forest
(a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the
result in any order.

---

We may traverse on the given binary tree to detect whether current node is
marked for deletion.

At each node, we check whether current node is marked for deletion. However, we
need to collect the roots of the new trees as well. We can also check for this
by whether we have deleted previously. If the node has been deleted (has no
parent) "and" is not marked for deletion, current node becomes the root of the
new tree - we can add this to our result.

Then, we traverse to left and right, carrying the information about whether we
have current node deleted. As we come out, we are adjusting the pointers from
left and right as well via deciding to return current node based on whether we
have current node marked for deletion.

Both time and space complexity would be O(n) as we need to visit each nodes and
build our result upto O(n) where n are number of nodes present.

---

Python:

```python

class Solution:
    def deleteNodes(self, root, toDelete):
        toDelete = set(toDelete)
        result = list()

        def helper(node, hasParent):
            if not node:
                return None
            
            deleteCurrent = node.val in toDelete
            # is current node start of new tree?
            if not (hasParent or deleteCurrent):
                result.append(node)

            # traverse down while propagating next results in recursion
            node.left = helper(node.left, not deleteCurrent)
            node.right = helper(node.right, not deleteCurrent)

            # return node iff it is not marked for deletion
            return node if not deleteCurrent else None

        helper(root, False)

        return result
```
