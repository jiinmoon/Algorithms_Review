""" 23. Merge k Sorted Lists

Question:

    Given a list of sorted linked lists, merge them into one.

+++

Solution:

    Simplest approach would be repeat the merge two algorithm over k-1
    iterations. This is O(k * (m+n)) algorithm that can be improved further
    with a simple twist. We pair up the lists and merge them together before
    moving on - this reduces the depth to lg K.

"""

class Solution:
    def mergeTwo(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if not l1 and not l2:
            return None
        dummyHead = curr = ListNode(float('-inf'))
        while l1 or l2:
            if l1.val < l2.val:
                temp = l1
                l1 = l1.next
            else:
                temp = l2
                l2 = l2.next
            curr.next = temp
            curr = curr.next
        curr.next = l1 or l2
        return dummyHead.next

    def mergeKLists(self, lists):
        while lists:
            temp = []
            while lists:
                l1 = lists.pop()
                l2 = lists.pop() if lists else None
                temp.append(self.mergeTwo(l1, l2))
            lists = temp
        return lists
