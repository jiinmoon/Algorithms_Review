""" 148. Sort List

Question:

    Sort a linked list in O(n lg n) using constant space complexity.

+++

Solution:

    We can achieve this sorting in-place via MergeSort algorithm. This is done
    by first find the mid point to split the linked list into two halves. Then,
    we recursively sort the list of two halves repeatedly. Then, we merge the
    two lists starting from single nodes.

"""


class Solution:
    def merge(self, list1, list2):
        dummyHead = curr = ListNode(float('-inf'))
        while list1 or list2:
            if list1.val < list2.val:
                temp = list1
                list1 = list1.next
            else:
                temp = list2
                list2 = list2.next
            curr.next = temp
            curr = curr.next
        curr.next = list1 or list2
        return dummyHead.next

    def findMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        return head2

    def sortList(self, head):
        if not head or not head.next:
            return head

        head2 = self.findMid(head)
        list1 = self.sortList(head)
        list2 = self.sortList(head2)
        head = self.merge(list1, list2)

        return head
