# 445 Add Two Numbers II

class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

    def addTwoNumbers(self, l1, l2):
        if not (l1 and l2):
            return l1 or l2

        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        carry = 0

        prev = None
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            newNode = Node(carry % 10)
            newNode.next = prev
            prev = newNode
            carry //= 10

        return prev

