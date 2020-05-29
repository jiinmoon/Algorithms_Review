""" 61. Rotate List

Question:

    Given a linked list, rotate the list to te right by k places, where k is
    non-negative.

+++

Solution:

    First, we should traverse to find the k-th node to identify the new head of
    the list and new tail - in fact, the k-th node will be the new head of the
    list. Then it is a matter of reconfiguring the next pointers of newHead to
    head, and newTail to None.

"""

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head

        listLength = self.length(head)
        steps = k % listLength
        newHead = newTail = head

        for _ in range(steps):
            newHead = newHead.next

        # find positin of newTail.
        while newHead.next:
            newHead = newHead.next
            newTail = newTail.next

        # newHead is at now end of list; reattach back to head.
        newHead.next = head
        # newHead should be back to newTail's next.
        newHead = newTail.next
        # newTail should be the end of list.
        newTail.next = None

