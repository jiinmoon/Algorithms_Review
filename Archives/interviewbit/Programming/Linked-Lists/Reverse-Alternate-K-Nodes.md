# Reverse Alternate K Nodes

    Given a linked list A of length N and an integer B.

    You need to reverse every alternate B nodes in the linked list A.

---

## Approach:

We can solve this problem with recursion; first, we reverse the first section
of the B groups. Then, we skip forward B steps. If there are more nodes to
process, we recursively repeat the process.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def reverseAlternate(self, head, k):

        if not (head and head.next):
            return head
        
        # reverse first k steps
        # if not enough, reverse as far out as possible
        prev, curr = None, head
        for _ in range(k):
            if not curr:
                break
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head.next = curr 

        # skip forward k steps; move to previous to K-th
        for _ in range(k - 1):
            if not curr:
                break
            curr = curr.next

        # more nodes to process? reverse next part recursively
        if curr:
            curr.next = self.reverseAlternate(curr.next, k)
        
        # return head of the new reversed list
        return prev
```

