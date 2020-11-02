# 19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list
and return its head.

Follow up: Could you do this in one pass?

---

Since we are not given the length of the list, we appear to be foreced to
traverse at least once to find the length to identify the Nth position to fix
the list. However, we can avoid this by first having a runner move forward upto
N times. Then, traverse on the list until this runner reaches Null - in which
case we will have our second runner that starts normally be placed at the
previous to the target node to remove. It could be the case that we may remove
the head as well - prepare the dummy node to accomodate for this edge case.

---

Python:

```python

class Solution:
    def removeNthFromBehind(self, head, n):
        if not head:
            return head

        runner = head
        for _ in range(n):
            runner = runner.next
        
        dummyHead = prev = ListNode(None)
        dummyHead.next = head
        while runner:
            runner = runner.next
            prev = prev.next
        prev.next = prev.next.next
        return dummyHead.next
```

