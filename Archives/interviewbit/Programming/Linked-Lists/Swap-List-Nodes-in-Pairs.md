# Swap List Nodes in Pairs

    Given a linked list, swap every two adjacent nodes and return its head.

    For example,

    Given 1->2->3->4, you should return the list as 2->1->4->3.

    Your algorithm should use only constant space. You may not modify the values in
    the list, only nodes itself can be changed.

---

Python:

```python

class Solution:

    def swapPairwise(self, head):

        if not (head and head.next):
            return head

        dummy = prev = ListNode(None)
        dummy.next = head

        while prev.next and prev.next.next:
            a, b, c = prev.next, prev.next.next, prev.next.next.next

            prev.next = b
            b.next = a
            a.next = c
            prev = a
        
        return dummy.next
```
