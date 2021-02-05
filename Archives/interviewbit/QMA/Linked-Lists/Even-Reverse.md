# Even Reverse

Given a linked list A , reverse the order of all nodes at even positions.

---

Split the given list into two lists where one has odd index'd elements and
other even index'd elements. Reverse the even list, then weave the two lists
together. O(n) in time complexity and O(1) in space.

---

Python:

```python

class Solution:

    def evenReverse(self, head):

        def split(node):
            dummyOdd = prevOdd = ListNode(None)
            dummyEven = prevEven = ListNode(None)
            k = 1
            while node:
                if k % 2:
                    prevOdd.next = node
                    node = node.next
                    prevOdd = prevOdd.next
                else:
                    prevEven.next = node
                    node = node.next
                    prevEven = prevEven.next
                k += 1
            prevOdd.next = None
            prevEven.next = None

            return dummyOdd.next, dummyEven.next

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
            flip = True
            while l1 and l2:
                if flip:
                    prev.next = l1
                    l1 = l1.next
                else:
                    prev.next = l2
                    l2 = l2.next
                flip = not flip
                prev = prev.next
            prev.next = l1 or l2
            return dummy.next

        oddHead, evenHead = split(head)
        evenHead = reverse(evenHead)
        return weave(oddHead, evenHead)
```
