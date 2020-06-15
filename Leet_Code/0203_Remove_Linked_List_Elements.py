""" 203. Remove Linked List Elements """

class Solution:
    def removeElements(self, head, val):
        if not head:
            return
        # instead of curr, prev would be more appropriate.
        dummyHead = curr = ListNode(float('-inf'))
        dummyHead.next = head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummyHead.next
