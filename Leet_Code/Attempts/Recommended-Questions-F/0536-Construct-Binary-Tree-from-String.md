# 536. Construct Binary Tree from String

You need to construct a binary tree from a string consisting of parenthesis and
integers.

The whole input represents a binary tree. It contains an integer followed by
zero, one or two pairs of parenthesis. The integer represents the root's value
and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it
exists.

---

We may approach this problem recursively while thinking of the problem as
a combination of a stack manipulation and dfs. First we convert the given
string into a stack. As we recursively move down on the given tree (iterate
from left to right on the given string), we first check for whether we have
a number of parenthesis. If the first character we encounter is a num, then we
try to build as far right as possible while converting the character into the
num. This will build our current node. Then, if we encounter open parenthesis,
we traverse to left (preorder) to bulid the node's left subtree. And again, if
we again encounter open parenthesis, we traverse to right for node's right
subtree. Finally, when we encounter closing parenthesis, we pop the current
character to continue and return our node.

The time complexity of this problem should be O(n).

---

Python:

```python

class Solution:
    def str2tree(self, s):
        def helper():
            if s and (s[0].isdigit() or s[0] == "-"):
                num = s.popleft()
                while s and s[0].isdigit():
                    num += s.popleft()
                currNode = TreeNode(int(num))
            if s and s[0] == "(":
                s.popleft()
                currNode.left = helper()
            if s and s[0] == "(":
                s.popleft()
                currNode.right = helper()
            if s and s[0] == ")":
                s.popleft()
            return currNode
                
        if not s:
            return s

        s = collections.deque(list(s))
        return helper()
```
