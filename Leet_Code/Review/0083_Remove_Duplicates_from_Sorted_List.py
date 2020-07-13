""" 83. Remove Duplicates from Sorted List

Question:

    Given a sorted linked list, delete all duplicates such that each element
    appear only once.

+++

Solution:

    We will have a scanner that moves forward until it has encountered a new
    element.

"""

class Solution:
    def delete_duplicates(self, head):
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

