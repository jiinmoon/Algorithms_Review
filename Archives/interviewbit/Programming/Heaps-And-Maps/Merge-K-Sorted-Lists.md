# Merge K Sorted Lists

    Merge k sorted linked lists and return it as one sorted list.

---

## Approach:

Naively, we could iteate on every head of the lists to find the minimum to
extend upon, this would be O(k * n) in time complexity. We can improve upon
this by using the heap.

Merging process can take upto n times, but we only have to perform heap
operation until pq is left or log(k) effectively as we are reducing the size of
merging each time. Hence, O(n * log(k)) in time complexity.

Another approach would be to pair up each two lists and continuously merging
them. As size of lists to merge reduces by half each time, it too has a time
complexity O(n * log(k)).

---

Python:

```python

from heapq import heapify, heappop, heappush

class Solution:

    def mergeKLists(self, A):

        pq = [(node.val, i) for i, node in enumerate(A) if node]
        heapify(pq)

        dummy = prev = ListNode(None)

        while pq:
            val, i = heappop(pq)

            prev.next = ListNode(val)
            prev = prev.next

            if A[i].next:
                A[i] = A[i].next
                heappush(pq, (A[i].val, i))

        return dummy.next
```
