""" 25. Reverse Nodes in K Group

Question:

    Given a linked list, reverse the nodes of a linked list k at a time and
    return its modified list.

"""

class Solution:
    def reverseKGroup(self, head, k):
        # check whether current length is enough for k group.
        nextHead = head
        for _ in range(k):
            if not nextHead:
                return head
            nextHead = nextHead.next
        # recursive call here; go all the way down until we cannot reverse.
        prev = self.reverseKGroup(nextHead, k)
        curr = head
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

