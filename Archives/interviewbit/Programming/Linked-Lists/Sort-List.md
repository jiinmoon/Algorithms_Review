# Sort List

    Sort a linked list in O(n log n) time using constant space complexity.

---

We can use merge sort to perform sort in-place. Recursively divide the array
into equal halves until single node is left. On the way up, merge two divided
lists.

---

Python:

```python

class Solution:

    def mergeSort(self, head):

        if not (head and head.next):
            return head

        def merge(l1, l2):
            
            if not (l1 and l2):
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

            prev.next = l1 or l2
            
            return dummy.next

        prev, slow, fast = head, head, head

        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next

        prev.next = None
        l1 = self.mergeSort(head)
        l2 = self.mergeSort(slow)

        return merge(l1, l2)
```

