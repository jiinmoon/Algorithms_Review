""" 160. Intersection of Two Linked Lists

Question:

    Write a program to find the node at which the intersection of two singly
    linked lists begins.

+++

Solution:

    The basic idea would be same as finding the cycle - we create an cycle by
    connecting the end of the list to each others starting point.

"""

class Solution:
    def getIntersectingNode(self, head1, head2):
        if not head1 or not head2:
            return None

        runner1, runner2 = head1, head2
        while runner1 != runner2:
            runner1 = runner1.next if runner1 else head2
            runner2 = runner2.next if runner2 else head1

        return runner1
