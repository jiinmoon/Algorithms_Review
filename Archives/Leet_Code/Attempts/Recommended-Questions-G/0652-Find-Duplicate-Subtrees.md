# 652. Find Duplicate Subtrees

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of
any one of them.

Two trees are duplicate if they have the same structure with the same node
values.

---

This can be best approached as a grouping problem. At each of the nodes that we
traverse down to and visit, we further generate the ordered list of current
subtree. Then, we record this subtree ordering in a hashmap where value would
be the root of this subtree representation (current node).

As we need to generate subtree at each node, the overall time complexity
becomes O(n^2). The space would occupy O(n).

---

Python:

```python

class Solution:
    def findDuplicateSubtrees(self, root):
        if not root:
            return []

        # key = string representation of subtree
        # value = list of root of sharing same subtree representation
        record = collections.defaultdict(list)

        def helper(node):
            if not node: return "Null"
            # build subtree representation with current node as root
            subtree = str(node.val)
            left = helper(node.left)
            right = helper(node.right)
            subtree = ",".join([subtree, left, right])
            # record current subtree representation to its root
            record[subtree].append(node)
            return subtree

        helper(root)

        result = list()
        # gather duplicate subtree roots
        for _, nodes in record.items():
            if len(nodes) > 1:
                result.append(nodes[0])

        return result
``` 
