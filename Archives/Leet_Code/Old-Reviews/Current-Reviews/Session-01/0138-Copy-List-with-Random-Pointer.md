138 Copy List with Random Pointer
=================================

A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. 

Each node is represented as a pair of [val, random\_index] where:

    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) where random
    pointer points to, or null if it does not point to any node.


---

The problem with the random pointer is that it can reference a node that is
further behind in the list - thus, this requires us to deal with several cases
if we are to do it in a single iteration.

If the current node is not in the record of our copied nodes, then we create
a copy of the current node and add to the record (`record[curr]
= ListNode(...`).

If the current node has next pointer, then we check whether we have made a copy
of the node pointed by the next pointer in the record. If it does not exist,
then we create the copy of next node and add to the record, as well as update
the copied node'next pointer in the record as well.

If the curret node has random pointer, then repeat the process same as above.

---

Python:

```python
class Solution:
    def copyRandomList(self, head):
        if not head: return
        curr = head
        record = dict()
        while curr:
            if curr not in record:
                record[curr] = Node(curr.val, None, None)
            if curr.next: 
                if curr.next not in record:
                    record[curr.next] = Node(curr.next.val, None, None)
                record[curr].next = record[curr.next]
            if curr.random:
                if curr.random not in reocrd:
                    record[curr.random] = Node(curr.random.val, None, None)
                record[curr].random = record[curr.random]
            curr = curr.next
        return record[head]
```

