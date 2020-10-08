# 753 Cracking the Safe

There is a box protected by a password. The password is a sequence of n digits
where each digit can be one of the first k digits 0, 1, ..., k-1.

While entering a password, the last n digits entered will automatically be
matched against the correct password.

For example, assuming the correct password is "345", if you type "012345", the
box will open because the correct password matches the suffix of the entered
password.

Return any password of minimum length that is guaranteed to open the box at
some point of entering it.

---

The problem can be viewed as a directed graph; each node contains the last
n - 1 digits of the pattern that must satisfy - then, nodes will form k edges
where it is labeled by the possible digits. Thus, each node plus its out-degree
edge will form a full pattern of a password.

Then, our task here is to find a path that visits every possible edges on this
graph - which we call it Euclerian path (or trail) in graph theory. To find
such path, we perform dfs to explore as far as possible.

---

Python:

```python

class Solution:
    def crackSafe(self, n, k):
        visited, result = set(), list()
        digits = [str(i) for i in range(k)]

        def helper(node):
            for digit in digits:
                nextNode = node + digit
                if nextNode not in visited:
                    visited.add(nextNode)
                    helper(nextNode[1:])
                    result.append(digit)

        dfs("0" * (n - 1))
        return "".join(result) + "0" * (n-1)
```
