# Merge two sorted Linked Lists
#
# Question:
#
# Write a SortedMerge() function that takes two lists, each of which is sorted
# in increasing order, and merges the two together into one list which is in
# increasing order. SortedMerge() should return the new list. The new list
# should be made by splicing together the nodes of the first two lists.
# For example if the first linked list a is 5->10->15 and the other linked list
# b is 2->3->20, then SortedMerge() should return a pointer to the head node of
# the merged list 2->3->5->10->15->20.
# There are many cases to deal with: either ‘a’ or ‘b’ may be empty, during
# processing either ‘a’ or ‘b’ may run out first, and finally, there’s the
# problem of starting the result list empty, and building it up while going
# through ‘a’ and ‘b’.
#
# ---
#
# Attempt:
#
# We iterate on both of the lists. Compare current two front nodes and append
# whichever is smaller onto our new linked list to build. Take care of the case
# where the lengths of the lists are uneven - in which case, we append to our
# returning list whichever is remaining after merging process.
#
# Time complexity : O(m + n) where m and n are length of lists.
# Space complexity : O(1) as we are splicing existing nodes from given lists.

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def mergeLists(self, A, B):
    # either is empty; return whichever exist
    if not (A and B):
        return A or B

    dummy = prev = ListNode(None)
    while A and B:
        if A.val < B.val:
            temp = A
            A = A.next
        else:
            temp = B
            B = B.next
        prev.next = temp
        prev = prev.next

    prev.next = A or B
    return dummy.next
