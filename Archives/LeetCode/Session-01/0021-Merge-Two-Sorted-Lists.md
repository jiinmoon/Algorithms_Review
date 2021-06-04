# 21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. The list should
be made by splicing together the nodes of the first two lists.

---

We can merge two sorted linked lists in O(m + n) time by iterating on both
lists at the same time, comparing the current nodes. Then, splice the whichever
node that is smaller unto the new list to be returned.

---

Python:

```python

class Solution21:

    def mergeTwo(self, l1, l2):

        if not (l1 or l2):
            return l1 or l2

        dummy = prev = ListNode(None)

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # edge case where uneven length of lists are given
        # whichever is left over is spliced in the end
        prev.next = l1 or l2

        return dummy.next
```

Java:

```java

class Solution21
{
    public ListNode mergeTwo(ListNode l1, ListNode l2)
    {
        if (Objects.isNull(l1) || Objects.isNull(l2))
            return (Objects.isNull(l2)) ? l1 : l2;

        ListNode dummy, prev;
        dummy = prev = new ListNode();

        while (Objects.nonNull(l1) && Objects.nonNull(l2))
        {
            if (l1.val <= l2.val) {
                prev.next = l1;
                l1 = l1.next;
            } else {
                prev.next = l2;
                l2 = l2.next;
            }
            prev = prev.next;
        }

        prev.next = (Objects.nonNull(l1)) ? l1 : l2;

        return dummy.next;
    }
}
```
