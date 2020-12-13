# Reorder List

Given a singly linked list

L: L0 → L1 → … → Ln-1 → Ln,

reorder it to:

L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

You must do this in-place without altering the nodes’ values.

---

To perform zig-zag swapping, we first traverse to mid node, and split the given
array into two halves. Reverse the second half of the array and weave the nodes
toegether into a single list.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def reorderList(self, A):

        # find half way point
        prev, slow, fast = None, A, A

        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        
        # split and start reversing second half
        prev.next = None
        secondA = None

        while slow:
            temp = slow.next
            slow.next = secondA
            secondA = slow
            slow = temp

        # weave
        flip = False
        dummy = prev = ListNode(None)

        while A and secondA:
            if flip:
                prev.next = secondA
                secondA = secondA.next
            else:
                prev.next = A
                A = A.next
            flip = not flip
            prev = prev.next

        # move over left overs
        prev.next = A or secondA

        return dummy.next

```

