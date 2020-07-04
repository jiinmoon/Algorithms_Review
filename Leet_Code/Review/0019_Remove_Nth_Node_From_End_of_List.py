""" 19. Remove Nth Node From End of List

Question:

    Given a linked list, remove the Nth node from the end of list, and return
    its head.

+++

Solution:

    To find out where Nth node is placed, we would have to once iterate to find
    the length of the linked list. Or alternatively, we may have a runner
    placed Nth step forward such that we can have another pointer moving at the
    same pace; when runner has reached end, our pointer will be at prev to the
    Nth node.

"""

class Solution:
    def removeNthFromEnd(self, head, n):
        if not head:
            return
        # iterate to find Nth Node
        runner = head 
        while n:
            runner = runner.next
            if not runner:
                # invalid n; not in range. 
                return
            n -= 1
        
        dummyHead = curr = ListNode(float('-inf'))
        while runner:
            runner = runner.next
            curr = curr.next
        curr.next = curr.next.next
        return dummyHead.next


