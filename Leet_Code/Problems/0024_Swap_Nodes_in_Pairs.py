""" 24. Swap Nodes in Pairs

Question:

    Given a linked list, swap every two adjacent nodes and return its head.

+++

Solution:

    We can create as many temporary pointers as we would like - then it is all
    about taking step-by-step, reattaching the next pointers.

"""

class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        dummyHead = prev = ListNode(-1)
        dummyHead.next = head
        while prev.next and prev.next.next:
            A, B, C = prev.next, prev.next.next, prev.next.next.next
            prev.next = B
            B.next = A
            A.next = C
            prev = A
        return dummyHead.next
