1110 Delete Nodes And Return Forest
===================================

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to\_delete, we are left with a forest
(a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the
result in any order.

---

We recurisvely traverse down on the tree; if the node is not marked for delete
and also does not have a parent, we can add it to the result. Then, we
recursively build current node's left and right. We can complete this traversal
in O(n).

---

Python:

```python
class Solution:
    def delNodes(self, root, to_delete):
        def helper(node, hasParent):
            if not node: return
            delete = node.val in to_delete
            if not hasParent and not delete:
                res.append(node)
            # prev was marked for deletion?
            # children should have no parent
            node.left = helper(node.left, not delete)
            node.right = helper(node.right, not delete)
            return node if not delete else None

        res = list()
        to_delete = set(to_delete)
        
        helper(root, False)
        return res
```

