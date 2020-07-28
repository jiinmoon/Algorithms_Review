86 Partition List
=================

Question:
---------

Given a linked list and a value x, partition it such that all nodes less than
x come before nodes greater than or equal to x. Preserve the relative old
ordering.

Solutions:
----------

Simply, we will create two new list where we will append the nodes under and
greater values to each. Then, concatenate both together in the end.

Codes:
------

Python:

```python
class Solution:
    def partition(self, head, x):
        dummyHead1 = curr1 = ListNode(None)
        dummyHead2 = curr2 = ListNode(None)
        while head:
            if head.val < x:
                curr1.next = head
                curr1 = curr1.next
            else:
                curr2.next = head
                curr2 = curr2.next
            head = head.next
        curr1.next = dummyHead2.next
        curr2.next = None
        return dummyHead1.next
```

---

**Source:**

LeetCode: [Partition-List](https://leetcode.com/problems/partition-list)
