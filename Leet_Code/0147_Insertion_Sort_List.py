""" 147. Insertion Sort Linked List

Question:

    Sort a linked list using the insertion sort.

+++

Solution:

    Remember that the insertion sort works by growing the 'sorted' region from
    left to right. We first move forward to find the next element to be
    'inserted' into this sorted region.

"""

class Solution:
    def insertionSortList(self, head):
        if not head or not head.next:
            return head

        dummyHead = ListNode(float('-inf'))
        prev = dummyHead
        curr = head
        while curr:
            # save pointer to continue on.
            temp = curr.next
            # find insertion position in sorted region.
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            # insert current node between prev/prev.next
            # (since prev.n.val > curr.val).
            curr.next = prev.next
            prev.next = curr
            # restore prev back to prev of start of list.
            prev = dummyHead
            # curr moves back to previous saved pointer.
            curr = temp
        return dummyHead.next
