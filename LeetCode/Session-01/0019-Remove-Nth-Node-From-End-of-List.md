# 19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list
and return its head.

Follow up: Could you do this in one pass?

---

We may think that we are required to first at least iterate the given list once
to determine total length of the linked list, and then traverse to find the
N-th node from behind. However, we can do this in a single pass with a trick
where we have a runner that is initially placed N-th place forward. By the time
that this runner has reached the end of the list, we have another runner that
was moving at the same rate but from the very beginning would be placed before
the n-th node. In either cases, the overall time complexity would be O(n).

---

Python: Single-pass approach.

```python

class Solution19:

    def removeNthFromEnd(self, head, n):

        runner = head
        for _ in range(n):
            runner = runner.next
        
        # edge case where head is the N-th node to remove
        # hence, dummy is required here
        dummy = prev = ListNode(None)
        dummy.next = head

        while runner.next:
            runner = runner.next
            prev = prev.next

        prev.next = prev.next.next
        
        return dummy.next
```
