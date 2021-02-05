# Reverse Linked List II

    Reverse a linked list from position m to n. Do it in-place and in one-pass.

    For example:

    Given 1->2->3->4->5->NULL, m = 2 and n = 4,

    return 1->4->3->2->5->NULL.

---

## Approach:

Iterate forwrad m steps and start reverse process for (n - m) steps. Make sure
to save the previous pointer to where reversal happened in order to reattach
the new head of the reversed list back to the original list.

---

Python:

```python

class Solution:

    def reverseBetween(self, head, m, n):

        if not (head and head.next):
            return head

        dummy = prev = ListNode(None)
        dummy.next = head

        for _ in range(m - 1):
            prev = prev.next

        newHead, newTail = None, prev.next

        for _ in range(n - m + 1):
            temp = newTail.next
            newTail.next = newHead
            newHead = newTail
            newTail = temp
        
        # prev.next is still pointing at the last ndoe of the reversed list
        prev.next.next = newTail
        prev.next = newHead

        return dummy.next
```
