""" 86. Partition List

Question:

    Given a linked list and a value x, partition it such that all nodes less
    than x come before nodes greater than or equal to x.

    You should preserve the original relative order of the nodes in each of the
    two partitions.

+++

Solution:

    We prepare a two lists - one where we keep the values less than x and
    another greater than x. Then, we attach the two lists.

"""

class Solution:
    def partition(self, head, x):
        if not head or not head.next:
            return head

        dummyHead1 = curr1 = ListNode(float('-inf'))
        dummyHead2 = curr2 = ListNode(float('-inf'))
        dummyHead1.next = curr1
        dummyHead2.next = curr2

        while head:
            if head.val < x:
                curr1.next = ListNode(head.val)
                curr1  = curr1.next
            else:
                curr2.next = ListNode(head.val)
                curr2 = curr2.next
            head = head.next

        curr1.next = dummyHead2.next
        curr2.next = None

        return dummyHead1.next
