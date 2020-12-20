# Rotate List

    Given a list, rotate the list to the right by k places, where k is
    non-negative.

    For example:

    Given 1->2->3->4->5->NULL and k = 2,
    return 4->5->1->2->3->NULL.


---

## Approach:

First, we compute the length of the given list to find the kth place where
rotation needs to occur. As K can be unexpectedly large, we should modulo. 

O(n) in time complexity.

---

Python:

```python

class Solution:

    def rotateRight(self, head, k):

        length, curr = 0, head
        while curr:
            length += 1
            curr = curr.next

        k %= length
        
        newHead, newTail = head, head
        for _ in range(k):
            newHead = newHead.next

        while newHead.next:
            newhead = newHead.next
            newTail = newTail.next

        newHead.next = head
        newHead = newTail.next
        newTail.next = None

        return newHead
```
