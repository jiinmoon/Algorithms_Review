""" 2.2 Return Kth To Last

Question:

    Implement an algorithm to find the kth to last element of a singly linked
    list.

---

We would need a further clearification on whether k value will always be within
acceptable bounds (if not, do we loop around?).

Since we are only given the list and not its length, the intuition is to at
least traverse the list once to determine the length to find the node at the kth
position. However, there is a trick to this question that can save us a bit of
time by using extra pointer.

Basically, we prepare a pointer to move Kth step forward. Then, when this
pointer hits the end, then we know that curr pointer that lagged behind will be
exactly at Kth position; thus, granting us to simply return the contents of its
node without having to scan once again to find the Kth node.

"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def returnKthToLast(self, head, k):
        """ assume k is valid """
        runner = head
        while k:
            runner = runner.next
            k -= 1
        while runner:
            runner = runner.next
            head = head.next
        return head

