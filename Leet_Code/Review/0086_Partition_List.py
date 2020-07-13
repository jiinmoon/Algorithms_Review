""" 86. Partition List

Question:

    Given a linked list and a value x, partition this list such that all nodes
    less than x comes before the nodes greater than x.

+++

Solution:

    Let's prepare a two list: lesser and greater. We will append all nodes less
    than x to the lesser and likewise for nodes greater than x tot greater.
    Then, we will merge the two lists at the end.

"""

class Solution:
    def partition(self, head, x):
        l1 = curr1 = ListNode(None)
        l2 = curr2 = ListNode(None)
        while head:
            if head.val < x:
                curr1.next = head
                curr1 = head
            else:
                curr2.next = head
                curr2 = head
            head = head.next
        curr2.next = None
        curr1.next = l2.next
        return l1.next
