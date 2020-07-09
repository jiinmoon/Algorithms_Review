""" 61. Rotate List

Question:

    Given a linked list, rotate the list to the right by k places, where k is
    non-negative.

+++

Solution:

    Firstable, we traverse on the list to find the k-th node to find the new
    head of the list and new tail - k-th node is the new head of the list.

"""

class Solution:
    def length(self, head):
        result = 0
        while head:
            result += 1
            head = head.next
        return result

    def rotate_right(self, head, k):
        # does not make sense to rotate on list with single node
        if not head or not head.next:
            return head
        # find the k-th node
        # k can be greater than list length; need to wrap around
        list_length = self.length(head)
        step = k % list_length
        newHead = newTail = head

        for _ in range(step):
            newHead = newHead.next

        # find newTail position
        while newHead.next:
            newHead = newHead.next
            newTail = newTail.next

        # newHead is at end of list
        newHead.next = head
        newHead = newTail.next
        newTail.next = None
        return newHead
