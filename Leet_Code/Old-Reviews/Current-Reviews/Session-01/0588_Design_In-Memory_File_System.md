588 Design In-Memory File System
================================

Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that
only contains this file's name. If it is a directory path, return the list of
file and directory names in this directory. Your output (file and directory
names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new
directory according to the path. If the middle directories in the path don't
exist either, you should create them as well. This function has void return
type.

addContentToFile: Given a file path and file content in string format. If the
file doesn't exist, you need to create that file containing given content. If
the file already exists, you need to append given content to original content.
This function has void return type.

readContentFromFile: Given a file path, return its content in string format.

---

The idea is as follows: we view this file system almost akin to a Trie
structure.

Have a root "/" directory be an object, Dir. This object will maintain
a hashmap of children directories that lead to other sub directories.

Also, we will maintain a map of { filePath : content } so that we can
retrieve/update contents of the file easily. Hence, the Dir() just there so
that we can keep track of how the directory structure is laid out - has little
to not bearing on the files themselves.

---

Python:

```python
# think as Trie
class Dir:
    def __init__(self)
        # { dirName : Dir }
        self.children = dict()

class FileSystem:
    def __init__(self):
        self.root = Dir()
        # { filePath : content }
        self.files = dict()

    def ls(self, path):
        # single file? (i.e. /a/b/c/d)
        if path in self.files:
            return [path.split("/")[-1]]
        # otherwise, move down to sub_dir and retrieve the childrens
        else:
            path = path.split("/")
            currDir = self.root
            for subDir in path[1:]:
                currDir = currDir.children[subDir]
            # lexicographically sorted
            return sorted(list(currDir.children.keys()))

    def mkdir(self, path):
        # move down the path while creating Dir
        path = path.split("/")
        currDir = self.root
        for subDir in path[1:]:
            if subDir not in currDir.children:
                currDir.children[subDir] = Dir()
            currDir = currDir.children[subDir]

    def addContentToFile(self, filePath, content):
        if filePath not in self.files:
            self.files[filePath] = content
            path = filePath.split("/")
            currDir = self.root
            for subDir in path[1:-1]: # stop before last which is a fileName
                currDir = currDir.children[subDir]
            currDir.children[path[-1]] = None # mark as file
        else:
            self.files[filePath] += content

    def readContentFromFile(self, filePath):
        return self.files[filePath]

```


