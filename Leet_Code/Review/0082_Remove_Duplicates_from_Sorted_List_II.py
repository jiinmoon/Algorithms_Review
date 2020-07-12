""" 82. Remove Duplicates from Sorted List II

Question:

    Givne a sorted linked list that may contain duplicates, delete all nodes
    which are duplicates including itself.

+++

Solution:

    We will make a new head where we will append the non-duplicate node as
    follows:

    Choose a node, and while this node has a duplicate, we move forward to find
    the first occurrence of the non-duplicate node. Then, we reattach the prev
    node to the non-duplicate node and repeat the process until end of the
    list.

"""

class Solution:
    def remove_duplicates(self, head):
        dummyHead = prev = ListNode(float('-inf'))
        dummyHead.next = head
        curr = head
        while curr:
            # duplicate found; move forward until new.
            if curr.next and curr.val == curr.next.val:
                dup_val = curr.val
                curr = curr.next
                while curr and curr.val == dup_val:
                    curr = curr.next
                # nothing is added to the new list.
                prev.next = None
            else:
                # curr is new value; safe to add to new list.
                prev.next = curr
                prev = curr
                curr = curr.next
        return dummyHead.next
                
