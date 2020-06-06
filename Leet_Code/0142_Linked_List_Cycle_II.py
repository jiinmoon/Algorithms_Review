""" 142. Linked List Cycle II

Question:

    Given a linked list with a cycle, return the node where cycle begins.

"""

class Solution:
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # cycle found. restart from head until fast is none.
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return fast
        return none
