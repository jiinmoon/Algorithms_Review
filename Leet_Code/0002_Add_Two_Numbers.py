""" 2. Add Two Numbers

Question:

    You are given two non-empty linked lists representing two non-negative
    integers. The digits are stored in reverse order and each of their nodes
    contain a signle digit. Add the two numbers and return it as a linked list.

+++

Solution:

    While we may directly add the integers and create the list at the same time,
    we can practice good software design principle - and create few helper
    functions to help us organize and keep our logic straight forward.

"""

class Solution:
    def listToInt(self, head):
        result = i = 0
        while head:
            result += head.val * 10 ** i
            head = head.next
            i += 1
        return result

    def intToList(self, num):
        dummyHead = curr = ListNode(float('-inf'))
        dummyHead.next = curr
        while num:
            curr.next = ListNode(num % 10)
            curr = curr.next
            num //= 10
        return dummyHead.next

    def addTwoNumbers(self, l1, l2):
        if not l1 and not l2:
            return None
        if not l1 or not l2:
            return l1 or l2
        result = self.listToInt(l1) + self.listToInt(l2)
        return self.intToList(result)
