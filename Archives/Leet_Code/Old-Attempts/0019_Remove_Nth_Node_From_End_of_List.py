""" 19. Remove Nth Node From End of List

Question:

    Given a linked list, remove the n-th node from the end of list and return
    its head.

"""

class Solution:
    def removeNthFromEnd(self, head, n):
        if not head:
            return None

        runner = head
        while n:
            runner = runner.next
            if not runner:
                return None
            n -= 1

        # dummy is requied as we could be removing head.
        dummyHead = curr = ListNode(-1)
        dummyHead.next = head
        while runner:
            curr = curr.next
            runner = runner.next
        curr.next = curr.next.next
        return dummyHead.next
