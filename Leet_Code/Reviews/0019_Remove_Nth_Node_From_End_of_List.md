19 Remove Nth Node From End of List
===================================

Question:
---------

Given a linked list, remove n-th node from end of list and return its head.


Solutions:
---------

The first problem is finding that n-th node. We could iterate the linked list
once to find its length and compute the number of steps required to reach the
n-th node via (len - n), but better way would be to simply place the runner
pointer that is ahead n steps forward. When this runner reaches the end, the
other pointer which is n steps behind would be at prev to n-th node, allowing
us to delete the next n-th node with ease.

Codes:
------

Python3:

```python
class Solution:
    def removeNthFromEnd(self, head, n):
        if not head or not head.next:
            return head
        # prepare a runner.
        runner = head
        while n:
            runner = runner.next
            n -= 1
        dummyHead = curr = ListNode(None)
        dummyHead.next = head
        # find nth node.
        while runner:
            runner = runner.next
            curr = curr.next
        curr.next = curr.next.next
        return dummyHead.next
```

---

**Source:**

LeetCode: [Remove-Nth-Node-From-End-of-List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
