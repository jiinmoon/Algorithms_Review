""" 21. Merge Two Sorted Lists

Question:

    Given two linked lists, merge them together and return as one linked list.

+++

Solution:

    Merging two linked list is an easy process of continually check the two
    heads' values, and append them to the new head.

"""

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if not l1 and not l2:
            return None
        dummyHead = curr = ListNode(float('-inf'))
        while l1 or l2:
            if l1.val < l2.val:
                temp = l1
                l1 = l1.next
            else:
                temp = l2
                l2 = l2.next
            curr.next = temp
            curr = curr.next
        curr.next = l1 or l2
        return dummyHead.next

