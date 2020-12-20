# Insertion Sort List

    Sort a linked list using insertion sort.

---

## Approach:

Iterate forward; if we see that next node's value is out of place - that is,
next node is less than the current node, then we start our insertion process.
Otherwise, we can simply move forward.

For insertion sort, we first skip over the next node while saving pointer to
the next node. Then, start from the head, we iterate to find the correct place
where the target node is to be inserted.

O(n * log(n)) in time complexity.

---

Python:

```python

class Solution:

    def sortList(self, head):

        dummy = prev = ListNode(float('-inf'))
        dummy.nex = head

        while prev.next:

            curr = prev.next

            if curr.val >= prev.val:
                prev = prev.next
                continue

            runner = dummy
            while runner.next.val <= curr.val:
                runner = runner.next

            curr.next = runner.next
            runner.next = curr

        return dummy.next
```
