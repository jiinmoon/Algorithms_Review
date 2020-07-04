""" 25. Reverse Nodes in k-Group

Question:

    Given a linked list and k, reverse the nodes in k groupings.

+++

Solution:

    There are many approaches, but we will use a recursive solution since this
    is a reverse process simply repeated over k groups.

"""

class Solution:
    def reverseNodesInKGroups(self, head, k):
        nextHead = head
        for _ in range(k):
            if not nextHead:
                return head
            nextHead = nextHead.next

        prev = self.reverseNodesInKGroups(nextHead, k)
        curr = head
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev.next = curr
            curr = temp
        return prev

