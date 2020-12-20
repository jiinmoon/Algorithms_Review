# Even Reverse

    Given a linked list A , reverse the order of all nodes at even positions.

---

## Approach:

Split the given array into odd and even list. Reverse the even and weave back
together.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def evenReverse(self, head):

        if not (head and head.next):
            return head

        def split(node):
            dummy1 = prev1 = ListNode(None)
            dummy2 = prev2 = ListNode(None)
            k = 1
            while node:
                if k % 2:
                    prev1.next = node
                    prev1 = prev1.next
                else:
                    prev2.next = node
                    prev2 = prev2.next
                node = node.next
                k += 1
            prev1.next = None
            prev2.next = None
            return dummy1.next, dummy2.next


        def reverse(node):
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev

        def weave(l1, l2):
            dummy = prev = ListNode(None)
            flip = False
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

        oddHead, evenHead = split(head)
        evenHead = reverse(evenHead)
        
        return weave(oddHead, evenhead)
```
