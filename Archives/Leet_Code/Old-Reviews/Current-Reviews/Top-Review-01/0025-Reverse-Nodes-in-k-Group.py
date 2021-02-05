# 25 Reverse nodes in k Group
#
# Use recursion.

class Solution:
    def reverseKGroup(self, head, k):
        if not head or k < 2:
            return head

        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next

        prev = self.reverseKGroup(curr, k)
        for _ in range(k):
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev
