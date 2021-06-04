# 19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list
and return its head.

Follow up: Could you do this in one pass?

---

Normally, we would require the length of the entire list in order to find
whether current node is the nth node from behind. This implies two-pass
approach, but we can do this in a single pass by first prepare a runner that is
Nth paces forward. Then, we have another runner start from the head and move
both at the same time. By the time that the first runner has reached the end,
we would have a second runner following behind placed at Nth node from the end.

---

Python:

```python

class Solution19:

    def removeNthFromBehind(self, head, n):

        if not head:
            return None

        runner = head
        for _ in range(n):
            if not runner:
                return None
            runner = runner.next
        
        # Nth node can be head of the list
        dummy = prev = ListNode(None)
        dummy.next = head

        while runner:
            runner = runner.next
            prev = prev.next

        prev.next = prev.next.next

        return dummy.next
```

