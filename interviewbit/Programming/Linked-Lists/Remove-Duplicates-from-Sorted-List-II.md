# Remove Duplicates from Sorted List II

    Given a sorted linked list, delete all nodes that have duplicate numbers,
    leaving only distinct numbers from the original list.

    For example,

    Given 1->2->3->3->4->4->5, return 1->2->5.
    Given 1->1->1->2->3, return 2->3.

---

## Approach:

Since we have to delete all of the duplicated segment, we maintain the dummy
(as head may also get removed) as well as previous node pointer to the next
node to be exaimned. So long as the current node val is same as next, we
iterate forward.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def removeDuplicates(self, head):

        if not (head and head.next):
            return head

        dummy = prev = ListNode(None)
        dummy.next = curr = head

        while curr:

            if curr.next and curr.val == curr.next.val:
                duplicate = curr.val
                curr = curr.next
                while curr and curr.val == duplicate:
                    curr = curr.next
                # remove pointer back to start of reversed segment
                prev.next = None
            else:
                prev.next = curr
                prev = curr
                curr = curr.next

        return dummy.next
```
