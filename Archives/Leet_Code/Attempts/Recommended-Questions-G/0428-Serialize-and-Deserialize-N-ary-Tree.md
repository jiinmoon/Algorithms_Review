# 428. Serialize and Deserialize N-ary Tree

Serialization is the process of converting a data structure or object into
a sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree
is a rooted tree in which each node has no more than N children. There is no
restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that an N-ary tree can be serialized to a string and
this string can be deserialized to the original tree structure.

---

Unlike binary tree, N-ary tree may have several of the children. Thus, while we
can follow the same traversal strategy (preorder in this case), we also need to
mark the positions where we have finished exploring all the children with
a identifier.

Thus, when we build it back up, we can first split the given data and reverse
it as we are recursively building it. For each node that we visit, we examine
the data given - until we encounter our identifier that inserted when we
serialized the tree, all the nodes upto that point should be the children of
the current node. Thus, we build the new node and add to our current node's
list of children.

---

Python:

```python

class Codec:
    def serialize(self, root):
        def helper(node):
            if not node:
                return
            result.append(str(node.val))
            for child in node.children:
                helper(child)
            result.append("#")

        result = list()
        helper(root)
        return ",".join(result)

    def deserialize(self, data):
        def helper(node):
            if not data:
                return None
            while data[-1] != "#":
                newNode = TreeNode(int(data.pop()), list())
                node.children.append(newNode)
                helper(newNode)
            # remove "#"
            data.pop()

        if not data:
            return None
        data = data.split(",")[::-1]
        root = TreeNode(int(data.pop()), list())
        helper(root)
        return root
```
