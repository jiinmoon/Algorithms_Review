""" 206. Reverse Linked List """

class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head
        # think prev.
        newHead = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = newhead
            newHead = curr
            curr = temp
        return newHead
