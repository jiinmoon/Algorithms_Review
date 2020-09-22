# 23 Merge k Sorted Lists
#
# Merging k Sorted lists is a log(k) repeated merging of the two lists.

class Solution:
    def mergeK(self, lists):
        if len(lists) > 1:
            temp = list()
            while lists:
                temp.append(self.mergeTwo(lists.pop(), lists.pop()))
            lists = temp

        return lists[0] if lists else None

    def mergeTwo(self, l1, l2):
        if not (l1 and l2):
            return l1 or l2

        dummy = prev = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                temp = l1
                l1 = l1.next
            else:
                temp = l2
                l2 = l2.next
            prev.next = temp
            prev = prev.next

        prev.next = l1 or l2
        return dummy.next
