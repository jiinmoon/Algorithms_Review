""" 2.4 Partition

Question:

    Write code to partition a linked list around a value x, such that all nodes
    less than x come before all nodes greater than or equal to x. If x is
    contained within the list, the values of x only need to be after the
    elements less than x. The partition element x can appear anywhere in the
    right partition; it does not need to appear between the left and right
    partitions.

---

The question is about dividing the list depending on the its value; there are
several ways to approach this:

    1. Keep track of back of the list; if the encountered value is greater, then
    we append to the back of the list.

    2. Keep a separate list that contains either only the less than, or greater
    values. Concatenate the two lists at the end and return.

"""

class ListNode:
    def __init__(self, val):


