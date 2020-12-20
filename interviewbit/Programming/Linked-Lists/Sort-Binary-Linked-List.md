# Sort Binary Linked List

    Given a Linked List A consisting of N nodes.

    The Linked List is binary i.e data values in the linked list nodes consist of
    only 0's and 1's.

    You need to sort the linked list and return the new linked list.

    NOTE:

    Try to do it in constant space.

---

## Approach:

Since we can replace the node's values, we can do this in-place by first
counting the number of ones. Then, starting from head, we skip over by amount
of zeros present, and start to place in 1s.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def sortBinaryLinkedList(self, head):

        curr, zeroes, ones = head, 0, 0

        while curr:
            zeroes += curr.val == 0
            ones += curr.val == 1
            curr = curr.next

        curr = head
        for _ in range(zeroes):
            curr.val = 0
            curr = curr.next

        for _ in range(ones):
            curr.val = 1
            curr = curr.next

        return head
```
