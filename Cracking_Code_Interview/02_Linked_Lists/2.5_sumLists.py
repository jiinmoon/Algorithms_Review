""" 2.5 Sum Lists

Question:

    You have two numbers represented by a linked list, where each node contains
    a single digit. The digits are stored in reverse order, usch that the 1's
    digit is at the head of the list. Write a function that adds the two numbers
    and returns the sum as a linked list.

    7 - 1 - 6 would be 617.

---

This is a striaght forward read, eval, and return an answer in linked list. But
what we want to emphasize here is the structure as to how we code this
particular problem. For example, we can try to be efficient and compute the sum
as we are reading digit by digit. But the computation can get confusing and
messy, and overall can appear to be highly unstructured.

In comparison, we can instead opt to create few smallar helper functions to
tackle this problem. We can divide the works as follows: read the list and
convert to integer; add two integers; return the integer as a linked list
format.

The point here is to excersie the readability for other coders and how to work
in a shared environment.

"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:

    def sumLists(self, l1, l2):
        if not l1 and not l2: return None
        num1 = self.listToInt(l1)
        num2 = self.listToInt(l2)
        return self.intToList(num1 + num2)

    def listToInt(self, head):
        if not head: return 0
        num, i = 0, 1
        while head:
            currDigit = head.val
            num += (currDigit * 10 ** i)
            i += 1
            head = head.next
        return num

    def intToList(self, num):
        if not num: return None
        dummyHead = currNode = ListNode(0)
        dummyHead.next = currNode
        currDigit = 0
        while num:
            currDigit = num % 10
            num = num // 10
            currNode.next = ListNode(currDigit)
            currNode = currNode.next
        return dummyHead.next



