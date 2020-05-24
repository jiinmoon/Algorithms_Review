""" 23. Merge k Sorted Lists

Question:

    Merge k sorted linked lists and return it as one sorted list.

+++

Solution:

    Again, we can view this problem as an extension on the merge 2 sorted list
    problem - but simply repeated over number of lists present. Hence, with this
    approach, the time complexity is O(kN) where k is the number of the lists.

    However, we could try to reduce the time further by pairing up the lists -
    and each iteration, we merge sort two lists for all. Then, we can complete
    the merging process in log(k) as number of lists to merge diminishes by half
    each time. This can effectively achieve O(N lg(k)) time complexity.

"""

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1 and not l2:
            return None
        if not l1 or not l2:
            return l1 or l2

        dummyHead = curr = ListNode(-1)
        dummyHead.next = curr

        while l1 and l2:
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
        while len(lists) > 2:
            temp = []
            while lists:
                l1 = lists.pop()
                l2 = lists.pop() if lists else None
                temp.append(self.mergeTwoLists(l1, l2))
            lists = temp
        return lists[0]
