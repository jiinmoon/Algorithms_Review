# 1206. Design Skiplist

Design a Skiplist without using any built-in libraries.

A Skiplist is a data structure that takes O(log(n)) time to add, erase and
search. Comparing with treap and red-black tree which has the same function and
performance, the code length of Skiplist can be comparatively short and the
idea behind Skiplists are just simple linked lists.

For example: we have a Skiplist containing [30,40,50,60,70,90] and we want to
add 80 and 45 into it. The Skiplist works this way:

Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons

You can see there are many layers in the Skiplist. Each layer is a sorted
linked list. With the help of the top layers, add , erase and search can be
faster than O(n). It can be proven that the average time complexity for each
operation is O(log(n)) and space complexity is O(n).

To be specific, your design should include these functions:

```
bool search(int target) : Return whether the target exists in the Skiplist or
not.

void add(int num): Insert a value into the SkipList. 

bool erase(int num): Remove a value in the Skiplist. If num does not exist in
the Skiplist, do nothing and return false. If there exists multiple num values,
removing any one of them is fine.
```

See more about Skiplist : https://en.wikipedia.org/wiki/Skip_list

Note that duplicates may exist in the Skiplist, your code needs to handle this
situation.

---

Let's think of Skiplist structure as a Tree Structure - Each node has a left
and right pointers. Left pointer goes to next depth where more elements are
populated and right pointers maintain the current list at each depth. Hence,
all we need to maintain is the root of this tree. 

Searching can be done from iterating from the root. While current node exist,
we try to expand as far right as possible. Either we can find the value in this
depth, or we arrive at the node that has a value less than target value for
searching. If so, then we try to move down a depth by going to the left and
repeat our search process.

Addition is a bit tricky. Here, we are first iterating to the depth where value
can be inserted. However, we also need to coin-toss to determine whether we
should also include this value from the depths bottom up. Hence, as we search
through, we maintain the previous depths' node where we have move down from;
this is where we should append new value to if we win the coin-toss. This can
be done with either recursion or stack. Also, we should remember to add another
depth to the list - otherwise it will always be depth of 1.

Process of deletion is reverse of addition - as we iterate to right at each
depth, we check to see whether value exist; if so, then we delete. However, we
may also have that same value below the depths as well! So, we should move
further down to delete all until bottom of the depth.

---

Python:

```python

class Node:
    
    # right goes to current depth list
    # left goes to depth below
    def __init__(self, val=float('-inf'), left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution1206:

    def __init__(self):
        self.root = Node()

    def search(self, target):

        curr = self.root

        while curr:
            # iterate to right to explore current depth
            while curr.right and curr.right.val < target:
                curr = curr.right
            # if it is the target, search is complete
            if curr.right.val == target:
                return True
            # otherwise, we continue this search from this point but below
            curr = curr.left

        return False

    def add(self, num):

        curr = self.root
        stack = list()      # maintain list of nodes prev to the num value

        while curr:

            # iterate to right to explore current depth to find first node
            # that is less than num; this is the insertion points
            while curr.right and curr.right.val < num:
                curr = curr.right

            stack.append(curr)

            # repeat same process till bottom of depths
            curr = curr.left

        # update tree
        # we should insert at depth where insertion point is found
        # then, use coin-toss to decide whether to continue to add them to depths above
        child = None
        insert = True
        while insert and stack:
            curr = stack.pop()
            curr.right = Node(num, child, curr.right)
            child = curr.right
            insert = random.random() < 0.5
        
        # remember to also add new depth
        if insert:
            self.root = Node(left=self.root)

    def erase(self, num):
        
        curr = self.root
        deleted = False

        # remember to remove all nodes 
        # - there may be duplicates present
        # - there can be same nodes below the depths
        while curr:

            while curr.right and curr.right.val < num:
                curr = curr.right

            if curr.right.val == num:
                curr.right = curr.right.right
                deleted = True
                # we do not stop here; go to left if there is

            curr = curr.left

        return deleted
```
