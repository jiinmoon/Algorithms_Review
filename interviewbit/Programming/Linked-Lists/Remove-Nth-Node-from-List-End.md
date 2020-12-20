# Remove Nth Node from List End

    Given a linked list, remove the nth node from the end of list and return its
    head.

    For example,

    Given linked list: 1->2->3->4->5, and n = 2.
    After removing the second node from the end, the linked list becomes
    1->2->3->5.

    Note:

    If n is greater than the size of the list, remove the first node of the list.

---

## Approach:

We do not have to traverse the entire list first in order to find the Nth node;
have a runner that moves up Nth step forward. Then, again, iterate forward
until the runner reaches the end. When the runner reaches the end of the list,
other runner will have reached the Nth node.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def removeNthBehind(self, head, N):
        
        slow = fast = head
        for _ in range(N):
            if not fast.next
                # remove first element if not valid N or exceeds
                return head.next
            fast = fast.next
        
        # move previous to Nth node
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return head
```
