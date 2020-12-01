# 1166. Design File System

You are asked to design a file system that allows you to create new paths and
associate them with different values.

The format of a path is one or more concatenated strings of the form:
/ followed by one or more lowercase English letters. For example, "/leetcode"
and "/leetcode/problems" are valid paths while an empty string "" and "/" are
not.

Implement the FileSystem class:

bool createPath(string path, int value) Creates a new path and associates
a value to it if possible and returns true. Returns false if the path already
exists or its parent path doesn't exist.
int get(string path) Returns the value associated with path or returns -1 if
the path doesn't exist.

---

We can create an Trie-like tree structure to store our subpaths as a separate
TrieNodes - and associate each wit hvalue if possible.

Time complexity would be O(n) due to having to traverse on each of the
previously created subpaths to either further create or get values of the
nodes.

We can improve the time complexity on get if we are to spend extra O(n) space
to store the values.

---

Python:

```python

class File:

    def __init__(self, content):
        self.children = dict()
        self.content = content

class Solution1166:

    def __init__(self):
        self.root = File()

    def createPath(self, path, value):
        # we can create a path to value iff previous paths have been created
        # move down the path as far as possible to check and retrieve until last path
        path = path.split("/")[1:]
        curr = helper(path[:-1])
        # either path is broken or already have a value associated with it
        if not curr or path[-1] in curr.children:
            return False        # ignore
        # otherwise, current path is valid
        curr.children[path[:-1]] = File(value)
        return True

    def helper(self, path):
        # for every subpath, traverse far down as possible
        curr = self.root
        for subpath in path:
            if subpath not in curr.children:
                return None
            curr = curr.children[subpath]
        return curr

    def get(self, path):
        curr = helper(apth.split("/")[1:])
        return curr.content if curr else -1
```

