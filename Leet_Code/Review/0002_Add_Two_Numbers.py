""" 2. Add Two Numbers

Question:

    Given two numbers in a linked list format, add the two numbers and return
    as a linked list.

+++

Solution:

    To me, the problem is not with manipualting the linked list, but about how
    to use a good design principle to maintain and share your code with your
    team. We can make this algorithm in a single function, but it would try to
    do much in a function. It has to parse the number from the linked list, add
    them, and convert back to linked list format. The better approach from
    design perspective would be to create several helper functions to keep it
    logically sane.

"""

class Solution:
    def listToInt(self, head):
        result = 0
        while head:
            result *= 10 + head.val
            head = head.next
        return result

    def intToList(self, num):
        dummyHead = curr = ListNode(float('-inf'))
        while num:
            curr.next = ListNode(num % 10)
            num //= 10
            curr = curr.next
        return dummyHead.next

    def addTwoNumbers(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        num1 = self.listToInt(l1)
        num2 = self.listToInt(l2)
        return self.intToList(num1 + num2)

