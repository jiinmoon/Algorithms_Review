293 Serialize and Deseralize Binary Tree
========================================

Serialization is the process of converting a data structure or object into
a sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no
restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and
this string can be deserialized to the original tree structure.

---

We will simply use preorder traversal to store the list. And when we rebuild,
repeat reverse process except ignoring "null"s that we encounter.

---

Python:

```python
class Code():
    def serialize(self, root):
        res = []

        def preorder(node):
            if not node:
                res.append("null")
            else:
                res.append(node.val)
                preorder(node.left)
                preorder(node.right)

        return ",".join(res)

    def deserialize(self, data):
        data = data.split(",")[::-1]

        def rebuild():
            if not data:
                return
            if data[-1] == "null":
                return
            node = TreeNode(data.pop())
            node.left = rebuild()
            node.right = rebuild()
            return node

        return rebuild()
```
