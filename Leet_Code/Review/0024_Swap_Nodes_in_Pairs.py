""" 24. Swap Nodes in Pairs

Question:

    Given a linked list, swap nodes pair-wise fashion.

+++

Solution:

    This is a basic manipulation of the linked list. The tip here is that we
    can create as many pointers that we can to save our nodes - so that we can
    keep our logics simple, and do not lose the pointers when we reconfigure
    them. Don't be a fool - always try to draw out the lists and try it on the
    paper first!

"""

class Solution:
    def swapNodesInPairs(self, head):
        if not head or not head.next:
            return head
        dummyHead = prev = ListNode(float('-inf'))
        dummyHead.next = head
        while prev.next and prev.next.next:
            A, B, C = prev.next, prev.next.next, prev.next.next.next
            prev.next = B
            B.next = A
            A.next = C
            prev = A
        return dummyHead.next

