""" 2.3 Delete Middle Node

Question:

    Implement an algorithm to delete a node in the middle (i.e., any node but
    the first and last node, not necessarily the exact middle) of a singly
    linked list, given only access to that node.

---

This can be perplexing to many as the typical way of delete a node from the
singly linked list is by knowing the previous node, and reassigning the next of
the previous node to skip the one that we are deleting.

Thus, the intuition is that you are forced to traverse the list to find the
previous node of the given node, then begin the deletion process.

However, there is a trick to this; that is you can modify the contents of the
node as you would see fit. Thus, if you are smart about it, you can delete the
given node with only access to that particular node by copying over the contents
(values) of the next node unto itself, then delete the node next to it which
would be a duplicate now.

"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def deleteMiddleNode(self, node):
        """ node is the middle node. """
        if not node or node.next: return node

        node.val = node.next.val
        node.next = node.next.next

