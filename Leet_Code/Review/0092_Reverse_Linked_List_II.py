""" 92. Reverse Linked List II

Question:

    Reverse a linked list from position m to n. Do it in one-pass.

+++

Solution:

    We move a pointer to m steps forward; then start the reverse process for (m
    - n) steps.

"""

class Solution:
    def reverse_between(self, head, m, n):
        if not head or m > n:
            return head
        prev, curr = None, head
        while m > 1:
            prev, curr = curr, curr.next
            m -= 1; n -= 1

        newHead, newTail = prev, curr

        while n >= 0:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            n -= 1

        if newHead:
            newHead.next = prev
        else:
            head = prev

        newTail.next = curr
        
        return head
