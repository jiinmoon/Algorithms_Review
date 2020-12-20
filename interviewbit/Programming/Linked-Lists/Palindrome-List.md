# Palindrome List

    Given a singly linked list, determine if its a palindrome. Return 1 or
    0 denoting if its a palindrome or not, respectively.

---

## Approach:

We split the array into two halves and reverse the either one. Then, iterate
while checking for the palindrome.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def isPalindrome(self, head):

        if not (head and head.next):
            return 1

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        def reverse(node):
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev

        head2 = reverse(slow)

        while head and head2:
            if head.val != head2.val:
                return 0
            head = head.next
            head2 = head2.next

        return 1
```
