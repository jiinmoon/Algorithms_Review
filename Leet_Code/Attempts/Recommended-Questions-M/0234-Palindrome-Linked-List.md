# 234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

---

One simple way to identify whether the given singly linked list is a palindrome
or not would be to create a integer or string representation of the linked list
by first iterating on it, and then determine whether it is a palindrome. This
would require O(n) extra space as well as it will take O(n) in time complexity.

Another method would be to reverse the half of the given linked list at its
centre, and start the comparison from start and the mid point. This would have
same time complexity as above, but will not require additional space.

---

Python:

```python

class Solution:
    def isPalindromeLinkedList(self, head):
        # identify mid point with runner
        fast = slow = head
        prev = None
        
        # fast moves twice as faster; reaching the end quicker
        # when fast reaches the end, slow is at mid point
        # here, while we move forward, we also reverse the first half
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # we can determine whether the list has odd or even length by checking
        # whether fast exists or not.
        # if fast exists, the slow is at exact mid element (odd length)
        # if fast is None, slow is positioned at beginning of second half (even length)
        if fast:
            slow = slow.next

        while slow:
            if slow.val != prev.val:
                return False
            slow = slow.next
            prev = prev.next

        return True
```

