""" 82. Remove Duplicates from Sorted List II

Question:

    Given a sorted linked list, delete all nodes that have duplicate numbers,
    leaving only distinct numbers from the original list.

"""

class Solution:
    def deleteDuplicates(self, head):
        # the head itself may contain duplicates.
        dummyHead = ListNode(float('-inf'))
        dummyHead.next = head
        prev, curr = dummyHead, dummyHead.next
        while curr and curr.next:
            if curr.val == curr.next.val:
                temp = curr.val
                while curr and curr.val = temp:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return dummyHead.next
