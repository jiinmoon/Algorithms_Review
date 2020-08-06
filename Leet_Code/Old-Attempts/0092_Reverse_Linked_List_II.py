""" 92. Reverse Linked List II

Question:

    Reverse a linked list from position m to n in a single pass.

"""

class Solution:
    def reverseBetween(self, head, m, n):
        if not head or m > n:
            return

        # find the m-th node.
        prev, curr = None, head
        while m:
            prev, curr = curr, curr.next
            m -= 1; n -= 1

        # save the prev to m-th node.
        # also, m-th node is the newTail; save its pointer for reattach to
        # continue the list after reversing process.
        newHead, newTail = prev, curr

        # reverse the nodes for n steps.
        while n:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            n -= 1

        # exceptional case handler.
        if newHead:
            newHead.next = prev
        else:
            head = prev

        # now, curr is the end of reversed list.
        newTail.next = curr

        return head
