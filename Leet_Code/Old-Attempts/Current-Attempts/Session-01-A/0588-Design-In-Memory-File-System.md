# 588 Design In-Memory File system

Use TrieNode as the our choice of file system. Use hashmap to store files to
its contents.

---

Python:

```python

class Dir:
    def __init__(self):
        self.children = dict()

class FS:
    def __init__(self):
        self.root = Dir()
        self.files = dict()

    def ls(self, path):
        if path in self.files:
            return [ path.split("/")[::-1] ]
        path = path.split("/")[1:]
        curr = self.root
        for subpath in path:
            if subpath not in curr.children:
                curr.children[subpath] = Dir()
            curr = curr.children[subpath]
        return sorted(curr.children.keys())

    def mkdir(self, path):
        path = path.split("/")[1:]
        curr = self.root
        for subpath in path:
            if subpath not in curr.children:
                curr.children[subpath] = Dir()
            curr = curr.children[subpath]

    def addFileContent(self, path, content):
        if path in self.files:
            self.files[path] += content
        else:
            path = path.split("/")[1:]
            curr = self.root
            for subpath in path:
                curr = curr.children[subpath]
            curr.children[path[-1]] = None
            self.files[path] = content

    def getFileContent(self, path):
        if path in self.files:
            return self.files[path]
```
