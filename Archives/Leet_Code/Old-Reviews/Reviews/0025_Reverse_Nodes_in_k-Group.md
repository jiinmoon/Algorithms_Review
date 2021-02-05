25 Reverse Nodes in k-Group
===========================

Question:
---------

Given a linked list, reverse the nodes k at a time and return new modified
list.

Solutions:
---------

First, we check to see whether there is enough k nodes in the given list
segment for us to reverse them. Then, at every k-th place, the next node is the
beginning of the new segment where the reversing process starts. Hence, we can
recursivly call our function again until we can find all the k-groups. Then, we
start the reverse process.

Codes:
------

Python:

```python
class Solution:
    def reverseKGroup(self, head, k):
        # determine whether k nodes.
        nextHead = head
        for _ in range(k):
            # not enough
            if not curr:
                return head
            nextHead = nextHead.next
        # repeat the process recursively on nextHead
        # It is the beginning of the new K-Group.
        prev = self.reverseKGroup(nextHead, k) 
        for _ in range(k):
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
```

---

**Source:**

LeetCode: [Reverse-Nodes-in-k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group)
