""" 83. Remove Duplicates from Sorted List

Question:

    Given a sorted linked list, delete all duplicates such that each element
    appear only once.

"""

class Solution:
    def deleteDuplicates(self, head):
        # unlike 81, we do not wish to delete all of them.
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
