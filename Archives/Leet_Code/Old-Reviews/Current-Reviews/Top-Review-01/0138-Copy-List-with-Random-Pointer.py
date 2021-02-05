# 138 Copy List with Random Pointer
#
# The problem is that random can point at the nodes far back in the list that
# we have not reached yet. To resolve this, we use hashmap structure to store
# individual nodes and fix the pointers as we encounter them.

class Solution:
    def copyListWithRandom(self, head):
        curr = head
        d = dict()

        while curr:
            if curr not in d:
                d[curr] = Node(curr.val, None, None)
            if curr.next:
                if curr.next not in d:
                    d[curr.next] = Node(curr.next.val, None, None)
                d[curr].next = d[curr.next]
            if curr.random:
                if curr.random not in d:
                    d[curr.random] = Node(curr.random.val, None, None)
                d[curr].random = d[curr.random]
            curr = curr.next

        return d[head]
