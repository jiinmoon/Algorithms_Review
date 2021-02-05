# BST Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be
initialized with the root node of a BST.

The first call to next() will return the smallest number in BST. Calling next()
again will return the next smallest number in the BST, and so on.

 Note: next() and hasNext() should run in average O(1) time and uses O(h)
 memory, where h is the height of the tree.

 Try to optimize the additional space complexity apart from the amortized time
 complexity. 

---

We can optimize this by storing the nodes in the stack. hasNext() can be O(1)
by checking whether stack is empty or not. next() can run in O(1) average as we
populate the stack again so long as node has a right subtree, in which case we
traverse again to left.

---

Python:

```python

class BSTIterator:

    def __init__(self, root):

        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left


    def hasNext(self):
        
        return len(self.stack) != 0


    def next(self):
        if not self.hasNext():
            return -1

        node = self.stack.pop()
        if node.right:
            curr = node.right
            while curr:
                self.stack.append(curr)
                curr = curr.left

        return node.val

```
