# 61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.

---

We can think of this problem differently - that is finding the k-th node from
the end of the list where it would become new head of the list.

But we have to think of several different cases here. First, we could have
a case where k is so large that finding k-th node naively would be a time
consuming operation. With naive implementation, we could have a case where we
would iterate the list over and over again. To fix this, we first iterate the
given list once to determine the length of the list, and then use modulo
operation.

Next, once we have found the k-th node from the end, we have to think about
what operations need to happen. We need the pointers to the previous to the new
head as well which becomes the new tail of the list so that we can properly
detach it from the new head of the list. As well, we should also iterate to the
end of the list so that we can attach it to the head of the given list and
return the new head of the list.

The time complexity of these operations should be linear.

---

Python:

```python

class Solution61:

    def rotateList(self, head, k):
        # trivial case
        if not (head and head.next):
            return head

        # measure length of given linked list
        length, runner = 0, head
        while runner:
            runner = runner.next
            length += 1

        # modulo to find k-th node from behind or new head of the rotated list
        k %= length

        newHead = newTail = head

        # find k-th to the end; new head of our rotated list
        for _ in range(k):
            newHead = newHead.next
        
        # move to "previous" to k-th place so that newTail is set to
        # prev to the k-th node which is the "new tail" of rotated list.
        while newHead.next:
            newHead = newHead.next
            newTail = newTail.next

        # loop our end of list to head
        newHead.next = head
        # set newHead to actual "new head" of rotated list.
        newHead = newTail.next
        # detach to avoid cycle
        newTail.next = None

        return newHead
```

