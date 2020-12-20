# Reorder List

    Given a singly linked list

    L: L0 → L1 → … → Ln-1 → Ln,

    reorder it to:

    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …


    You must do this in-place without altering the nodes’ values.


    For example,

    Given {1,2,3,4}, reorder it to {1,4,2,3}.



---

## Approach:

Split the given list into two equal halves. Reverse the later half, and weave
the two lists back into one.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def reorderList(self, head):

        if not (head and head.next):
            return head

        prev, slow, fast = head, head, head
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next

        prev.next = None

        def reverseList(node):
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev

        def weave(l1, l2):
            
            if not (l1 and l2):
                return l1 or l2

            flip = False
            dummy = prev = ListNode(None)
            while l1 and l2:
                if flip:
                    prev.next = l2
                    l2 = l2.next
                else:
                    prev.next = l1
                    l1 = l1.next
                flip = not flip
                prev = prev.next

            prev.next = l1 or l2
            return dummy.next

        head1 = head
        head2 = reverseList(slow)

        return weave(head1, head2)
```
            
