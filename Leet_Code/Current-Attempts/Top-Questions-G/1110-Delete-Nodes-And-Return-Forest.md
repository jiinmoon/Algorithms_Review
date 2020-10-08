# 1110 Delete Nodes And Return Forest

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to\_delete, we are left with a forest
(a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the
result in any order.

---

To delete all marked nodes in a binary tree, we need to be able to determine
whether the current node is marked for deletion. To be precise, we have to
determine whether there exists a "parent". If current node does not have
a parent and it is "not" marked for deletion, then this signals that current
node marks the beginning of a new subtree, which we should add to our list of
roots.

---

```python

class Solution:
    def deleteNodes(self, marked, root):
        result = list()
        marked = set(marked)

        def helper(node, hasParent):
            if not node:
                return
            isToDelete = node.val in marked
            if not hasParent and not isToDelete:
                result.append(node)
            node.left = helper(node.left, not isToDelete)
            node.right = helper(node.right, not isToDelete)
            return node if not isToDelete else None
        
        helper(root, False)
        return result
```
