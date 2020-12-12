# Remove Nth Node from List End

Given a linked list, remove the nth node from the end of list and return its
head.

For example,

Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes
1->2->3->5.

Note:

If n is greater than the size of the list, remove the first node of the list.

Try doing it using constant additional space.

---

We can use two runners; where one runner is placed n place forward. Then, when
we move two runners at same pace, when fast runner reaches end, slow runner
will be placed at n-th node.

Take care to note about n: if n is greater, we should simply remove first node.

O(n) in time complexity on single-pass.

---

Python:

```python

class Solution:

    def removeNthFromEnd(self, A, B):

        slow, fast = A, A

        for _ in range(B):
            if not fast.next:
                return A.next       # n greater than size of list; remove first
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return A

```
