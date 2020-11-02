# 25. Reverse Nodes in K Group

Given a linked list, reverse the nodes of a linked list k at a time and return
its modified list.

k is a positive integer and is less than or equal to the length of the linked
list. If the number of nodes is not a multiple of k then left-out nodes, in the
end, should remain as it is.

Follow up:

Could you solve the problem in O(1) extra memory space?
You may not alter the values in the list's nodes, only nodes itself may be
changed.

---

To reverse nodes in K grouping at a time, we use recursion. Using recursive
algorithm, we move down all the way to identify all the nodes in K groups;
then, building up, we start the reverse process. This algorithm is O(n) in time
complexity.

---

Python:

```python

class Solution:
    def reverseNodesKGroup(self, head, k):
        if not head or k < 2:
            return head

        curr = head
        for _ in range(k):
            if not curr.next:
                return head
            curr = curr.next

        prev = self.reverseNodesKGroup(curr, k)
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev
```
