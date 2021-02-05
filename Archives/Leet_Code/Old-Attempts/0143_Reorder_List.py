""" 143. Reorder List

Question:

    Given a singly linked list: 1 -> 2 -> 3 -> ... -> n-1, reorder it such that
    1 -> n-1 -> 2 -> n-2 -> ... .

+++

Solution:

    We split the given list into two halves, then reverse the second half of the
    list. Now, we can weave the two as one list to finish reordering process.

"""

class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return head

        # split into two halves.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None

        # reverse the later half of the list (head2).
        prev = None
        curr = head2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # reversed; prev is the new head of the second list.
        head2 = prev

        # weave the two list into one.
        while head2:
            temp1, temp2 = head.next, head2.next
            head.next = temp2
            head2.next = temp1
            head = temp1
            head2 = temp2

