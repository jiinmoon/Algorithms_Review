""" 21. Merge Two Sorted Lists

Question:

    Merge two sorted linked lists and return it as a new list. The new list
    should be made by splicing together the node sof the first two lists.

+++

Solution:

    This is the simplest form of K-Merge; intuitively, we can merge two sorted
    lists by comparing front elements and appending it to the new head. It
    should take O(m + n) time complexity.

"""

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1 and not l2:
            return None
        if not l1 or not l2:
            return l1 or l2

        dummyHead = curr = ListNode(-1)
        dummyHead.next = curr

        while l1 and l2:
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
