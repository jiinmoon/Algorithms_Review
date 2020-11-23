""" 2.1 Remove Dups

Question:

    Write code to remove duplicates from an unsorted linked list.

---

Since the linked list is unsorted, we have two choices as to delete the
duplicates; 1. use nested loop that checks for duplicated elements for every
element we visit in the list; and 2. use an extra structure to store information
about what previous elements we have seen and delete if we did.

Boh has a advantages and disadvantages. First approach is what we are forced to
use if extra memory buffer is not allowed, thus it would take more time. Second
approach would take upwards n space, but gurantees linear time complexity.

"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def removeDups_1(self, head):
        """ Using extra record data struct. O(n) space/time. """
        record = {}
        prevNode = None
        while head:
            if record.get(head.val, -1) != -1:
                prevNode.next = head.next
            else:
                record[head.val] = 1
                prevNode = head
            head = head.next

    def removeDups_2(self, head):
        """ Without using extra memory. O(1) space but O(n^2) time. """
        currNode = head
        while currNode:
            scanNode = currNode
            while scanNode:
                if scanNode.val == currNode.val:
                    scanNode.next = scanNode.next.next
                else:
                    scanNode = scanNode.next
            currNode = currNode.next

