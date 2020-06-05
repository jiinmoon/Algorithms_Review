""" 138. Copy List with Random Pointer

Question:

    A linked list is given such that each node contains an additional random
    pointer which could point to any node in the list or null.

    Return a deep copy of the list.

+++

Solution:

    While copying the simple linked list will be a trivial task, the problem is
    with the 'random' pointer that which points back to anywhere on the list.

    Thus, as we are iterating on the list, we need to think carefully about how
    we should approach this problem.

    First, if the current node has not been encountered beforehand, then we can
    create a copy of it and record it.

    Then, if the current node has a next, we can check whether current node's
    next already exists in the record. This is because of random pointer that we
    may have already created the copy and recorded it. If not, then we can
    create a copy, otherwise we can set the record[curr].next to
    record[curr.next].

    Now, we should check for whether current node has a random pointer. Again,
    if it does and random is not in the record, then we create it and record.

"""

class Solution:
    def copyRandomList(self, head):
        if not head:
            return

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
                if curr.random not in record:
                    record[curr.random] = Node(curr.random.val, None, None)
                record[curr].random = record[curr.random]
            curr = curr.next

        return record[head]
