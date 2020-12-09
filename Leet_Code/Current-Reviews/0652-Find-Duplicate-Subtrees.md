# 652. Find Duplicate Subtrees

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of
any one of them.

Two trees are duplicate if they have the same structure with the same node
values.

---

We codify each subtrees as we recursively traverse down on the nodes. We gather
root of these roots with matching subtrees in a hashmap. In the end, all the
root whose subtrees are shared will be grouped as a value in the hashmap.

Time complexity would be O(n^2) in order to create a codec for each node we
visit (traverse all the way down) and O(n^2) in space for hashmap as we need to
store n^2 subtrees.

---

Python:

```python

from collections import defaultdict

class Solution652:

    def findDuplicateSubtrees(self, root):

        def helper(node):

            if not node:
                return "None"

            subtree = ",".join([str(node.val), helper(node.left), helper(node.right)])
            record[subtree].append(node)

            return subtree


        record = defaultdict(list)

        helper(root)

        return [nodes[0] for nodes in record.values() if len(nodes) >= 2]
```


