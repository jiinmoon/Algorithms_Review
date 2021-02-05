# 297. Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into
a sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no
restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and
this string can be deserialized to the original tree structure.

---

Use preorder traversal to generate the serialized form of the given binary
tree. And reverse the process while performing same preorder traversal to
generate back the binary tree. Both operations should be O(n) in time
complexity.

---

Java:

```java

class Codec {
    
    public String serialize(TreeNode root) {
        List<String> result = new LinkedList<>();
        serializeHelper(root, result);
        return String.join(",", result);
    }

    private void serializeHelper(TreeNode node, List<String> result) {
        if (node == null) {
            result.add("Null");
        } else {
            result.add(Integer.toString(node.val));
            serializeHelper(node.left, result);
            serializeHelper(node.right, result);
        }
    }

    public TreeNode deserialize(String data) {
        Deque<String> nodes = new LinkedList<>(Arrays.asList(data.split(",")));
        return deserializeHelper(nodes);
    }

    private TreeNode deserializeHelper(Deque<String> nodes) {
        if (nodes.isEmpty()) return null;

        String curr = nodes.removeFirst();
        if (curr.equals("Null")) return null;

        TreeNode node = new TreeNode(Integer.valueOf(curr));
        node.left = deserializeHelper(nodes);
        node.right = deserializeHelper(nodes);

        return node;
    }
}

```

Python:

```python

class Solution:
    def serialize(self, root):
        def helper(node):
            if not node:
                result.append("Null")
                return
            result.append(str(node.val))
            helper(node.left)
            helper(node.right)
        result = list()
        helper(root)
        return ",".join(result)

    def deserialize(self, data):
        def helper():
            if not data:
                return
            val = data.pop()
            if val == "Null":
                return
            currNode = TreeNode(val)
            currNode.left = helper()
            currNode.right = helper()
            return currNode

        data = data.split(",")[::-1]
        return helper()
```
