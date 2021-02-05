# 297 Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into
a sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no
restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and
this string can be deserialized to the original tree structure.

---

Codec or compression of a data can be done in many ways; but here, we are going
to focus solely on codifying the structure of the binary tree and restoring it.
To do so, we simply perform a tree traversal to serialize; and to rebuild, we
reverse the traversal process. For example, if we used a preorder traversal to
serialize the tree, we can similarly use stack (or recursion) to rebuild the
same tree backwards. The both function will take linear amount of time.

---

Python:

```python

class Solution:
    def serialize(self, root):
        def helper(node):
            if not node:
                res.append("null")
                return
            res.append(str(node.val))
            helper(node.left)
            helper(node.right)

        res = list()
        helper(root)
        return ",".join(res)

    def deserialize(self, data):
        def helper():
            if not data or data[-1] == "null":
                return
            node = TreeNode(int(data.pop()))
            node.left = helper()
            node.right = helper()
            return node

        data = data.split(",")[::-1]
        return helper()
```
