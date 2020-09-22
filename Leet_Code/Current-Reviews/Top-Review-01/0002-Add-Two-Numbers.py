# 2 Add two Numbers
#
# Simply traverse on both with carry - time complexity should be O(m + n).

class Solution:
    def addTwoNumbers(self, l1, l2):
        if not (l1 and l2):
            return l1 or l2

        dummy = prev = ListNode(None)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            prev.next = ListNode(carry % 10)
            prev = prev.next
            carry //= 10

        return dummy.next
